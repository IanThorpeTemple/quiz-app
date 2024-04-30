import sqlite3
import os
import json

import requests
from flask import current_app

from ..db import get_db, close_db


class AddQuizzFromOpenQuizDb():
    """Add new quiz from openquizzdb.org"""
    URL_PREFIX = "https://download.openquizzdb.org"
    error_messages = {
        "bad_url" : "This a bad quiz url. Url need to be a openqizzdb.org download url",
        "bad_resp" : "This isn't a quiz from openquizzdb.org",
        "quiz_exists" : "Quiz with this name already exists",
        "bad_obj" : 'Not a valid python dict',
        "bad_img_url" : "This a bad image url",
        "missing_im_url" : "Provide an image url for the quiz"
    }

    def __init__(self, quiz_db_url:str, quiz_img:str=None) -> None:
        # openquizzdb download url
        self.url = quiz_db_url
        # Optionnal img for the quiz
        self.img_url = quiz_img
        # Quiz name
        self.quiz_title = ""
        # Quiz category
        self.quiz_category = ""
        # Quiz slogan
        self.quiz_slogan = ""
        # Python dict obtained from json response after request
        self.quiz_obj = {}
        # Key for quiz meta data
        self.meta_key = "catégorie-nom-slogan"
        # Key that contains all the quiz questions
        self.quest_data_key = "quizz"
        # Base language
        self.base_lang_code = 'en'
        # Meta data keys to get
        self.require_meta_keys = ["catégorie", "nom", "slogan"]
        # Quiz languages
        self.require_lang = ["fr", "en", "es"]
        # French quiz
        self.fr_quiz = {}
        # English quiz
        self.en_quiz = {}
        # Espanish quiz
        self.es_quiz = {}
        # Quiz levels
        self.require_level_for_lang = ["débutant", "confirmé", "expert"]
    

    def _valid_url(self):
        """Return True if the url is an openquizzdb.org url"""
        return self.url.startswith(self.URL_PREFIX)
    
    def _get_py_obj_or_none(self):
        """Make request on the url and get a python dict from the json response"""
        resp = requests.get(self.url)
        try:
            dict_resp = resp.json()
        except requests.exceptions.JSONDecodeError:
            return None
        else:
            return dict_resp
    
    def _valid_obj_format(self, obj) :
        """Return True and set quiz data if py_obj format obtained from openquizzdb.org is valid 
        and fill all the requirements otherwise the missing key(s).
        => Must be called before _create_new_quiz"""

        if not isinstance(obj, dict):
          return self.error_messages['bad_obj']  

        # Quiz meta data
        meta = obj.get(self.meta_key, None)
        meta_en = meta.get(self.base_lang_code, None) if meta else None

        if meta and meta_en:
            for key in self.require_meta_keys:
                if meta_en.get(key, None):
                    # Key exists
                    pass
                else:
                    return key
        else:
            return f"{self.meta_key},{self.base_lang_code}"
        
        # quiz datas
        quiz = obj.get(self.quest_data_key, None)
    
        if quiz:
            for lang in self.require_lang:
                if quiz.get(lang, None):
                    # quiz for this languague exists
                    quiz_lang = quiz.get(lang, None)
                    for level in self.require_level_for_lang:
                        if quiz_lang.get(level, None):
                            # has the rigth level
                            pass
                        else:
                            return level
                else:
                    return lang
        else:
            return self.quest_data_key

        self.quiz_obj = obj
        self._set_quiz_value()
        return True
    
    def _set_quiz_value(self):
        obj = self.quiz_obj

        self.quiz_category = obj[self.meta_key][self.base_lang_code][self.require_meta_keys[0]]
        self.quiz_title = obj[self.meta_key][self.base_lang_code][self.require_meta_keys[1]]
        self.quiz_slogan = obj[self.meta_key][self.base_lang_code][self.require_meta_keys[2]]

        self.fr_quiz = obj[self.quest_data_key][self.require_lang[0]] 
        self.en_quiz = obj[self.quest_data_key][self.require_lang[1]]
        self.es_quiz = obj[self.quest_data_key][self.require_lang[2]]

    def save_and_return_img_path(self):
        """Get the img from the given url and save it for the quiz by copying it.
        Return the url path that can be used to get the image. The
        return url can be used like this: http://domaine/{return_url}"""

        sub_direc = "quiz-images"
        img_view_url = current_app.config['IMAGE_URL']
        
        if self.img_url:
            try:
                response = requests.get(self.img_url)
            except: # Any exceptions
                return self.error_messages["bad_img_url"]
            else:
                resp_headers = response.headers
                content_type = resp_headers["Content-Type"].split('/')
                img_exten = content_type[1]
                if content_type[0].lower() != "image":
                    return self.error_messages['bad_img_url']
                
                path = f"{current_app.config['IMAGE_FOLDER_PATH']}/{sub_direc}"
                os.makedirs(path, exist_ok=True)
                with open(f"{path}/{self.quiz_title}.{img_exten}", "wb") as f:
                    f.write(response.content)
                
                return f"{img_view_url}{sub_direc}/{self.quiz_title}.{img_exten}"
        else:
            return self.error_messages['missing_im_url']

    def _create_new_quiz(self):
        """Create a new quiz in the db and return True 
        if not already exists else return False"""
        db = get_db()

        try:
            db.execute(
                "INSERT INTO quiz (title, category, slogan, image_url) VALUES (?, ?, ?, ?)",
                (self.quiz_title, self.quiz_category, self.quiz_slogan, self.img_url)
            )
            db.commit()
        except sqlite3.IntegrityError:
            # Quiz with this title already exists
            close_db()
            return False
        
        quiz_by_lang = {"fr" : self.fr_quiz, "en" : self.en_quiz, "es" : self.es_quiz}
        l_debu, l_conf, l_expe = self.require_level_for_lang

        for quiz_lang, quiz in quiz_by_lang.items():
            db.execute(
                """INSERT INTO quiz_data 
                (quiz_obj, lang, quest_debutant, quest_confirme, quest_expert) 
                VALUES (?, ?, ?, ?, ?)""", ( self.quiz_title, quiz_lang, json.dumps(quiz[l_debu]), 
                json.dumps(quiz[l_conf]), json.dumps(quiz[l_expe]) )
            )
            db.commit()
        
        close_db()
        return True

    def add_new_quiz_to_db(self):
        """Main method to fetch the quiz from the 
        openquizzdb.org url and add the quiz to the db.
        Returns True if quiz has been successfully added else an error message"""

        if(self._valid_url()):
            quiz_resp_ob = self._get_py_obj_or_none()
        else:
            return self.error_messages['bad_url'] 
        
        if quiz_resp_ob:
            is_valid_format = self._valid_obj_format(quiz_resp_ob)
        else:
            return self.error_messages['bad_resp']
        
        if not isinstance(is_valid_format, str):
            created = self._create_new_quiz()
        else:
            return self.error_messages['bad_resp']
        
        return created if created else self.error_messages['quiz_exists']

