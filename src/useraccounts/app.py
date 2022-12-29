"""
This module holds the function which retruns the instance of app.
"""

from flask  import Flask
from flask_pydantic_spec import FlaskPydanticSpec

from appscommon import logconfig

from useraccounts.bootstrap import bootstrap


logconfig.init()
api_spec = FlaskPydanticSpec('usersaccounts', title='Accounts API')

def main() -> Flask:
    """
    Creates flask app.

    Returns:
        app (Flask)
    """
    app = Flask(__name__)
    bootstrap(app=app)
    api_spec.register(app)

    return app
