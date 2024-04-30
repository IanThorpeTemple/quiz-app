"""Flask settings for FLASK Quiz APP"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

DATABASE = BASE_DIR / "quizz_app_db.sqlite3"

IMAGE_FOLDER_PATH = BASE_DIR / "images"
IMAGE_URL = "app-images/"

IN_PRODUCTION = False

