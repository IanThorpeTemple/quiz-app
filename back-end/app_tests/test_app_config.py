import sqlite3

import pytest
from flask import g, Flask

from app.db import get_db
from app.server import create_app


def test_get_close_db(app):
    with app.app_context():
        con = get_db()
        assert isinstance(g.db, sqlite3.Connection)
        assert isinstance(con, sqlite3.Connection)
        resul = con.execute("PRAGMA foreign_keys").fetchall()
        assert 1 == resul[0][0]

    with pytest.raises(sqlite3.ProgrammingError) as e:
        con.execute('CREATE TABLE quiz (title)')
    assert "closed database" in str(e.value) 


def test_app_factory(app):
    value = create_app()
    assert isinstance(value, Flask)
    assert "/static_files/build" in value.static_folder
    assert "/soft" == value.static_url_path