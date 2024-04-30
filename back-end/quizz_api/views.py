import json

from flask import Blueprint, current_app

from app.db import get_db

api_bp = Blueprint("api_bp", __name__)

db_level = {
    "débutant" : "quest_debutant",
    "confirmé" : "quest_confirme",
    "expert" : "quest_expert",
}

@api_bp.after_request
def do_after_request(response):
    if not current_app.config["IN_PRODUCTION"]:
        response.headers['Access-Control-Allow-Origin'] = "*"
    else:
        response.headers['Access-Control-Allow-Origin'] = "quiz-steel-omega.vercel.app"

    response.headers['Access-Control-Allow-Methods'] = "GET, POST"
    response.headers['Access-Control-Allow-Headers'] = "Content-Type"

    return response


@api_bp.route('all-categories/', methods=["GET"])
def all_categories():
    """Returns all available categories:
    >>> Response : {"categories" : ["category_name", ...]} 
    """
    db = get_db()
    categories = db.execute(
        "SELECT DISTINCT category FROM quiz ORDER BY category ASC"
    ).fetchall()

    response = {"categories" : []}
    for category in categories:
        response['categories'].append(category[0])

    return response

@api_bp.route('category-name/<title>/', methods=["GET"])
def get_quiz_cate_name(title):
    """Returns the category of the quiz that has this title.
    >>> Response : {"name" : "returned_category_name"}"""
    db = get_db()
    cate_name = db.execute(
        "SELECT category FROM quiz WHERE title=(?)", (title,)
    ).fetchall()
    
    response = {
        "name" : cate_name[0][0] if cate_name else ""
    }
    return response


@api_bp.route('all-quizs/', methods=["GET"])
def all_quizs():
    """Returns a list of all available:
    >>> Response : {"quizs" : [
            {
                "title" : "quiz_title", 
                "category" : "quiz_category", 
                "slogan" : "quiz_slogan",
                "image" : "img_url"
            }, ...
        ]} 
    """
    db = get_db()
    quizs = db.execute(
        """SELECT title, category, slogan, image_url
        FROM quiz ORDER BY title"""
    ).fetchall()

    response = {"quizs" : []}
    for quiz in quizs:
        quiz_obj = {
            "title" : quiz[0],
            "category" : quiz[1],
            "slogan" : quiz[2],
            "image" : quiz[3]
        }
        response["quizs"].append(quiz_obj)
        
    return response


@api_bp.route("cate-quiz/<category_name>", methods=['GET'])
def quiz_by_category(category_name):
    """Returns all quiz that have the given category
    >>> Response : {"quizs" : [
            {
                "title" : "quiz_title", 
                "category" : "quiz_category", 
                "slogan" : "quiz_slogan",
                "image" : "img_url"
            }, ...
        ]} 
    """
    db = get_db()
    quizs = db.execute(
        """SELECT title, category, slogan, image_url
        FROM quiz WHERE category=(?) ORDER BY title""", (category_name,)
    ).fetchall()

    response = {"quizs" : []}
    for quiz in quizs:
        quiz_obj = {
            "title" : quiz[0],
            "category" : quiz[1],
            "slogan" : quiz[2],
            "image" : quiz[3]
        }
        response["quizs"].append(quiz_obj)
    
    return response

@api_bp.route(
    "quiz/<quiz_title>/<lang>/<level>/", 
    methods=["GET"]
)
def quiz_data(quiz_title, lang, level):
    """Returns quiz data that contains all the questions and answers
    >>> Response : {"level" : quiz_data} """
    db = get_db()
    q_level = db_level[level]

    quiz_data = db.execute(
        f"SELECT {q_level} FROM quiz_data WHERE quiz_obj=(?) AND lang=(?)",
        (quiz_title, lang)
    ).fetchall()[0][0]

    response = {
        # Data was stored as a json formatted str
        level : json.loads(quiz_data) 
    }

    return response




