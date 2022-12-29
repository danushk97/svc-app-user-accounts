"""
This module holds the function which retruns the instance of app.
"""

from flask  import Flask

from common import logconfig

from useraccounts.bootstrap import bootstrap


logconfig.init()


def main() -> Flask:
    """
    Creates flask app.

    Returns:
        app (Flask)
    """
    app = Flask(__name__)
    bootstrap(app=app)

    return app
