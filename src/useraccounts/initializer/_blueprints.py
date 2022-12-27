"""
This module holds functions which helps to register blueprints.
"""

import importlib


BLUEPRINTS = [
    ('user_accounts.controller.user', 'user_app'),
    ('user_accounts.controller.auth', 'auth_app'),
    ('user_accounts.controller.password', 'password_app')
]


def register_blueprints(app):
    for module, blueprint_attr in BLUEPRINTS:
        module = importlib.import_module(module)
        blueprint = getattr(module, blueprint_attr)
        app.register_blueprint(blueprint)
