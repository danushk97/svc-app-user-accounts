"""
This module holds the function which retruns the instance of app.
"""
from flask  import Flask

from user_accounts.initializer import init_app


def create_app(di_configurator=None) -> Flask:
    """
    Creates flask app.

    Args:
        configure_di (function): Configuration function which helps to
        configure dependency injectors.

    Returns:
        app (Flask)
    """
    app = Flask(__name__)
    init_app(app, di_configurator)

    return app
