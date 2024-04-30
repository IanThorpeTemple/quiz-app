import os 

from flask import Flask, send_from_directory

from . import db
from .utils import commands
from quizz_api.views import api_bp


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object('app.settings')
    
    # Instance Path
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    app.teardown_appcontext(db.close_db)
    app.cli.add_command(commands.execute_sql_cmd)
    app.cli.add_command(commands.add_new_quiz_to_db)

    # Blueprint
    app.register_blueprint(api_bp, url_prefix="/api")

    img_url = app.config['IMAGE_URL']
    @app.route(f'/{img_url}/<image_name>', methods=["GET"])
    def get_image(image_name):
        return send_from_directory(
            app.config['IMAGE_FOLDER_PATH'], image_name
        )
    
    return app


if __name__ == "__main__":
    create_app().run(debug=True)