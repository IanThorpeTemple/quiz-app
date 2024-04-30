from unittest.mock import Mock
import os

import requests
from flask import current_app

from app.utils.add_quiz_to_db import AddQuizzFromOpenQuizDb
from .object import min_right_quiz_obj, bad_datas, bad_metas, resp_s
from app.db import get_db, close_db

class TestAddQuizToDb:
    good_url = "https://download.openquizzdb.org/3239275558"
    bad_url = "https://wiki.org/3239275558"
    right_instance = AddQuizzFromOpenQuizDb(
        good_url, "img_test_url"
    )
    bad_instance = AddQuizzFromOpenQuizDb(bad_url)
    test_quiz_title = resp_s['catégorie-nom-slogan']["en"]["nom"]
    db_init_scrip = """CREATE TABLE quiz(
                    title TEXT UNIQUE NOT NULL, 
                    category TEXT NOT NULL, 
                    slogan TEXT NOT NULL,
                    image_url TEXT NOT NULL
                ); CREATE TABLE quiz_data (
                    quiz_obj TEXT NOT NULL, 
                    lang TEXT NOT NULL, 
                    quest_debutant TEXT NOT NULL, 
                    quest_confirme TEXT NOT NULL, 
                    quest_expert TEXT NOT NULL,
                    FOREIGN KEY (quiz_obj) REFERENCES quiz (title) 
                    ON DELETE CASCADE ON UPDATE CASCADE
                );
                """

    def test_valid_url(self):
        """Right url testing"""
        assert self.right_instance._valid_url() == True
        assert self.bad_instance._valid_url() == False

    def test_get_py_obj_or_none(self):
        """Test if the method handle the exception and return the right value"""
        reqs = requests
        reqs.get = Mock(return_value=reqs.Response())

        # Error case
        reqs.Response.json = Mock(
            side_effect=reqs.exceptions.JSONDecodeError("error", "error", 1)
        )
        resp_obj = self.right_instance._get_py_obj_or_none()
        assert resp_obj == None
        reqs.get.assert_called_once_with(self.good_url)
        reqs.Response.json.assert_called_once()
        
        # without error
        reqs.Response.json = Mock(return_value={"test":1})
        resp_obj = self.right_instance._get_py_obj_or_none()
        assert resp_obj == {"test":1}
        assert reqs.get.call_count == 2
        reqs.get.assert_called_with(self.good_url)
        reqs.Response.json.assert_called_once()
    
    def test_valid_obj_format_for_inv(self):
        """"""
        # Bad metas
        for exp_key, bad_meta in bad_metas.items():
            assert self.right_instance._valid_obj_format(
                bad_meta
            ) == exp_key
        
        # Bad datas
        for exp_key2, bad_data in bad_datas.items():
            assert self.right_instance._valid_obj_format(
                bad_data
            ) == exp_key2
    
    def test_valid_obj_format_for_vali(self):
        # Valid format
        assert self.right_instance._valid_obj_format(
            min_right_quiz_obj
        ) == True
        
        # Check if self.right_instance._set_quiz_value defines the quiz values
        assert self.right_instance.quiz_obj == min_right_quiz_obj
        assert self.right_instance.quiz_title == min_right_quiz_obj["catégorie-nom-slogan"]["en"]["nom"]
        assert self.right_instance.quiz_category == min_right_quiz_obj["catégorie-nom-slogan"]["en"]["catégorie"]
        assert self.right_instance.quiz_slogan == min_right_quiz_obj["catégorie-nom-slogan"]["en"]["slogan"]
        assert self.right_instance.fr_quiz == min_right_quiz_obj["quizz"]["fr"]
        assert self.right_instance.en_quiz == min_right_quiz_obj["quizz"]["en"]
        assert self.right_instance.es_quiz == min_right_quiz_obj["quizz"]["es"]
    
    def test_save_and_return_img_path(self, app):
        with app.app_context():
            inst = self.right_instance
            requests.get = Mock(return_value=requests.Response)
            requests.Response.content = b'test'
            requests.Response.headers = {"Content-Type" : "image/jpeg"}
            inst.quiz_title = "test_quiz"
            
            # Test if return the desired path
            assert inst.save_and_return_img_path() == 'app-images/quiz-images/test_quiz.jpeg'

            # When error, must return none
            requests.get = Mock(side_effect=requests.exceptions.InvalidURL)
            assert inst.save_and_return_img_path() == inst.error_messages['bad_img_url']

            # Get method has been called
            requests.get.assert_called()

            # clean
            os.remove(
                os.path.join(
                    current_app.config['IMAGE_FOLDER_PATH'], "quiz-images", "test_quiz.jpeg"
                )
            )
            os.removedirs(
                os.path.join(
                    current_app.config['IMAGE_FOLDER_PATH'], "quiz-images"
                )
            )
    
    def test_create_new_quiz(self, app):
        """Test the method _create_new_quiz """
        add_quiz = self.right_instance
        add_quiz._valid_obj_format(resp_s)

        with app.app_context():
            con = get_db()
            con.executescript(self.db_init_scrip)
            con.commit()

            # Create a new quiz in the db
            assert self.right_instance._create_new_quiz() == True
            new_con = get_db()
            assert new_con.execute(
                f"SELECT quest_debutant FROM quiz_data WHERE quiz_obj=(?) AND lang=(?)",
                (self.test_quiz_title, "en")
            ).fetchall()[0][0]    

            # Create a quiz that already exist   
            assert self.right_instance._create_new_quiz() == False
            close_db()
            
    def test_add_new_quiz_to_db(self, app):
        """Test the main method (add_new_quiz_to_db) that is used
        to add a new quiz in the db """
        g_inst = self.right_instance

        # Url valildation
        bad_ins = self.bad_instance
        assert bad_ins.add_new_quiz_to_db() == bad_ins.error_messages["bad_url"]

        # Response data validation. Response must be a valid json and in a right format
        requests.get = Mock(return_value=requests.Response())
        # Valid json validation
        requests.Response.json = Mock(
            side_effect=requests.JSONDecodeError('error', "error", 2)
        ) 
        assert g_inst.add_new_quiz_to_db() == g_inst.error_messages['bad_resp']
        # Right format validation
        requests.Response.json = Mock(return_value=bad_datas['quizz'])
        assert g_inst.add_new_quiz_to_db() == g_inst.error_messages['bad_resp']
        requests.get.assert_called()
        requests.Response.json.assert_called()

        # Not creat a same quiz twice Validation
        with app.app_context():
            con = get_db()
            con.executescript(self.db_init_scrip)
            con.execute(
                "INSERT INTO quiz VALUES (?, ?, ?, ?)",
                (self.test_quiz_title, "en", "test_slogan", "test_img_url")
            )
            con.commit()
            requests.Response.json = Mock(return_value=resp_s)
            assert g_inst.add_new_quiz_to_db() == g_inst.error_messages['quiz_exists']
            close_db()
        
        # Right case
        with app.app_context():
            con = get_db()
            con.execute("DELETE FROM quiz WHERE title=(?)", (self.test_quiz_title,))
            con.commit()
            requests.Response.json = Mock(return_value=resp_s)
            assert g_inst.add_new_quiz_to_db() == True
            close_db()
        