from flask import Flask
from user_accounts import create_app

def test_create_app_should_return_instance_of_flask_app():
    app = create_app()
    assert isinstance(app, Flask)
