import sqlite3

import click
from ..db import get_db


from .add_quiz_to_db import AddQuizzFromOpenQuizDb


def execute_sql(sql):
    try:
        con = get_db()
        con.execute(sql)
        con.commit()
        click.echo("Command successfully executed")
    except sqlite3.Error as e:
        click.echo(f"❌❌❌❌❌❌ error ❌❌❌❌❌❌")
        click.echo(f"Sqlite error : {e}")

@click.command("exesql")
def execute_sql_cmd():
    """CLI to execute the given sql command in the Database"""
    while True:
        value = click.prompt("command to run (tape q to exit)")
        if str(value).lower() == "q":
            break
        execute_sql(value)

@click.command("addquiz")
def add_new_quiz_to_db():
    """Add new quiz to db or show an error message"""
    while True:
        value = click.prompt(
            "Quiz and Image link separate by a comma (tape q to exit)"
        )
        if str(value).lower() == "q":
            break
        
        links = value.split(",")
        if len(links) != 2:
            click.echo('Exactly two links, one for the quiz data and the last for the image')
            break

        quiz_link = links[0]
        img_link = links[1]
        result = AddQuizzFromOpenQuizDb(quiz_link, img_link).add_new_quiz_to_db()
        click.echo("Success") if isinstance(result, bool) else click.echo(result)
