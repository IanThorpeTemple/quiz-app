import tempfile
import os

import pytest

from app.server import create_app

@pytest.fixture
def app():
    db_fb, path = tempfile.mkstemp()
    app = create_app()
    app.config.update({
        "TESTING" : True,
        "DATABASE" : path,
    })

    yield app

    os.close(db_fb)
    os.unlink(path)

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def runner(app):
    return app.test_cli_runner()

