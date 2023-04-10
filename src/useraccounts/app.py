"""
This module holds the function which retruns the instance of app.
"""

from flask  import Flask
from flask_pydantic_spec import FlaskPydanticSpec

from appscommon import logconfig
from appscommon.flaskutils.confighelper import register_blueprints, register_http_error_handlers

from useraccounts.bootstrap import bootstrap
from useraccounts.entrypoints.rest import ROUTE_MODULES


logconfig.init_logging()
#  /apidoc/swagger
api_spec = FlaskPydanticSpec(
    'usersaccounts',
    title='Accounts API'
)


def flask_app() -> Flask:
    """
    Creates flask app.

    Returns:
        app (Flask)
    """
    bootstrap()
    app = Flask(__name__)
    register_http_error_handlers(app)
    register_blueprints(app, ROUTE_MODULES)
    api_spec.register(app)

    return app
