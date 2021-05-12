"""
This module holds the function which retruns the instance of app.
"""
from flask  import Flask
from flask_injector import FlaskInjector
from apputils.exception import AppException
from apputils.error_handler import ErrorHandler

from user_accounts.application.user_service import UserService
from user_accounts.application.validator.user_validator import \
    UserValidator
from user_accounts.application.error_code_generator \
    .invalid_user_error_code_generator import InvalidUserErrorCodeGenerator
from user_accounts.infrastructure.unit_of_work.postgres import \
    PostgresUnitOfWork
from user_accounts.infrastructure.sqlalchemy_session import \
    SQLAlchemySessionFactory
from user_accounts.controller.user import user_app
from user_accounts.controller.auth import auth_app
from user_accounts.controller.password import password_app


def configure_di(binder):
    """
    configures dependency injection.
    """
    binder.bind(UserService, UserService)
    binder.bind(PostgresUnitOfWork, PostgresUnitOfWork)
    binder.bind(InvalidUserErrorCodeGenerator, InvalidUserErrorCodeGenerator)
    binder.bind(UserValidator, UserValidator)


def register_blueprints(app: Flask) -> None:
    """
    Registers routes with the app instance.

    Args:
        app (Flask): Instance of app.
    """
    app.register_blueprint(user_app)
    app.register_blueprint(password_app)
    app.register_blueprint(auth_app)


def register_error_handlers(app: Flask) -> None:
    """
    Registers routes with the app instance.

    Args:
        app (Flask): Instance of app.
    """
    error_handler = ErrorHandler()
    app.register_error_handler(AppException, error_handler.app_error_handler)
    app.register_error_handler(Exception, error_handler.generic_error_handler)
    app.register_error_handler(404, error_handler.page_not_found_handler)
    app.register_error_handler(405, error_handler.method_not_allowed_handler)


def create_app(di_config=None) -> Flask:
    """
    Creates flask app.

    Args:
        test_di_config (function): Configuration function which helps to
                                   configure dependency injectors.

    Returns:
        app (Flask)
    """
    app = Flask(__name__)
    register_blueprints(app)
    register_error_handlers(app)

    #instansiating dependency injectors
    FlaskInjector(app, modules=[di_config or configure_di])

    return app
