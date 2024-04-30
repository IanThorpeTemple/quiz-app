from unittest.mock import Mock

import click
from app.utils.add_quiz_to_db import AddQuizzFromOpenQuizDb

def test_execute_sql_comm(runner, app):
    command = "exesql"
    # Test 'tape q to exit'
    click.prompt = Mock(return_value='q')
    result = runner.invoke(args=command)
    assert result.output == ''

    with app.app_context():
        # Error case
        click.prompt = Mock(side_effect=['CREATE title', "Q"])
        result = runner.invoke(args=command)
        assert "Sqlite error" in result.output 

        # Right case
        click.prompt = Mock(side_effect=['CREATE TABLE quiz (title)', "Q"])
        result = runner.invoke(args=command)
        assert "Command successfully executed" in result.output

def test_add_new_quiz_comm(runner):
    command = "addquiz"
    # Test 'tape q to exit'
    click.prompt = Mock(return_value="q")
    result = runner.invoke(args=command)
    assert result.output == ''

    # Missing one value
    click.prompt = Mock(side_effect=["test_url", "Q"])
    result = runner.invoke(args=command)
    assert 'Exactly two links, one for the quiz data' in result.output

    # Error message when adding new quiz
    click.prompt = Mock(side_effect=["test_url, img_test_url", "q"])
    AddQuizzFromOpenQuizDb.add_new_quiz_to_db = Mock(return_value='error message')
    result = runner.invoke(args=command)
    assert 'error message' in result.output
    AddQuizzFromOpenQuizDb.add_new_quiz_to_db.assert_called_once()
    # Right case
    click.prompt = Mock(side_effect=["test_url, img_test_url", "q"])
    AddQuizzFromOpenQuizDb.add_new_quiz_to_db = Mock(return_value=True)
    result = runner.invoke(args=command)
    assert "Success" in result.output


    

