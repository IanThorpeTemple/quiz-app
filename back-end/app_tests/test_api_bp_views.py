import json

import pytest
from flask import current_app

from app.db import get_db

def test_all_categories(client, app):
    with app.app_context():
        db = get_db()
        db.execute("CREATE TABLE quiz(title TEXT, category TEXT)")
        db.executemany(
            "INSERT INTO quiz (title, category) VALUES (?, ?)",
            [("Title1", "Cate1"), ("Title2", "Cate2"), ("Title3", "Cate1")]
        )
        db.commit()

        response = client.get("/api/all-categories/")
        assert response.status_code == 200
        assert json.loads(response.data) == {"categories" : ["Cate1", "Cate2"]}

        # Test the after request behavior
        headers_lis = [
            'Access-Control-Allow-Origin',
            'Access-Control-Allow-Methods',
            'Access-Control-Allow-Headers'
        ]
        for head in headers_lis:
            assert response.headers[head]

        current_app.config.update({
            'IN_PRODUCTION' : True
        })
        response = client.get("/api/all-categories/")
        for head in headers_lis:
            with pytest.raises(KeyError):
                response.headers[head]

def test_get_quiz_cate_name(client, app):
    with app.app_context():
        db = get_db()
        db.execute("CREATE TABLE quiz(title TEXT, category TEXT)")
        db.executemany(
            "INSERT INTO quiz (title, category) VALUES (?, ?)",
            [("Title1", "Cate1"), ("Title2", "Cate2"), ("Title3", "Cate1")]
        )
        db.commit()

        response = client.get("/api/category-name/Title1/")
        assert response.status_code == 200
        assert json.loads(response.data) == {"name" : "Cate1"}


def test_all_quizs_and_quiz_by_category(client, app):
    with app.app_context():
        db = get_db()
        db.execute(
            "CREATE TABLE quiz(title TEXT, category TEXT, slogan TEXT, image_url TEXT)"
        )
        db.executemany(
            "INSERT INTO quiz (title, category, slogan, image_url) VALUES (?, ?, ?, ?)",
            [("T1", "C1", "S1", "I1"), ("T2", "C2", "S2", "I2"), ("T3", "C2", "S3", "I3")]
        )
        db.commit()

        # all_quizs
        response = client.get("/api/all-quizs/")
        assert response.status_code == 200
        data = {"quizs" : [
            {"title" : "T1", "category" : "C1", "slogan" : "S1", "image" : "I1"},
            {"title" : "T2", "category" : "C2", "slogan" : "S2", "image" : "I2"},
            {"title" : "T3", "category" : "C2", "slogan" : "S3", "image" : "I3"},
        ]}
        assert json.loads(response.data) == data

        # quiz_by_category
        response2 = client.get("/api/cate-quiz/C2")
        assert response2.status_code == 200
        data2 = {"quizs" : [
            {"title" : "T2", "category" : "C2", "slogan" : "S2", "image" : "I2"},
            {"title" : "T3", "category" : "C2", "slogan" : "S3", "image" : "I3"},
        ]}
        assert json.loads(response2.data) == data2


def test_quiz_data(client, app):
    with app.app_context():
        db = get_db()
        db.executescript(
            """CREATE TABLE quiz(
                title TEXT UNIQUE, category TEXT, 
                slogan TEXT, image_url TEXT
            );
            CREATE TABLE quiz_data(
                quiz_obj TEXT, lang TEXT, 
                quest_debutant TEXT, quest_confirme TEXT,
                quest_expert TEXT,
                FOREIGN KEY (quiz_obj) REFERENCES quiz(title)
            );
            INSERT INTO quiz VALUES ("T1", "C1", "S1", "I1")
            """
        )
        db.executemany(
            "INSERT INTO quiz_data VALUES (?, ?, ?, ?, ?)",
            [
                (
                    "T1", "en", json.dumps("data_en_deb"), json.dumps("data_en_con"), 
                    json.dumps("data_en_exp")
                ), 
                (
                    "T1", "fr", json.dumps("data_fr_deb"), json.dumps("data_fr_con"), 
                    json.dumps("data_fr_exp")
                ),
                (
                    "T1", "es", json.dumps("data_es_deb"), json.dumps("data_es_con"), 
                    json.dumps("data_es_exp")
                ),
            ]
        )
        db.commit()

        response = client.get('/api/quiz/T1/en/débutant/')
        assert response.status_code == 200
        assert json.loads(response.data) == {"débutant" : "data_en_deb"}

        response = client.get('/api/quiz/T1/fr/expert/')
        assert response.status_code == 200
        assert json.loads(response.data) == {"expert" : "data_fr_exp"}