"""
This module holds functions which helps to configure dependency injection.
"""

from useraccounts.application.user_service import UserService
from useraccounts.application.validator.user_validator import UserValidator
from useraccounts.infrastructure.sqlalchemy.unit_of_work import SQLAlchemyUnitOfWork
from useraccounts.application.error_code_generator.invalid_user_error_code_generator import \
    InvalidUserErrorCodeGenerator


def di_configurator(binder):
    """
    configures dependency injection.
    """
    binder.bind(UserService, UserService)
    binder.bind(SQLAlchemyUnitOfWork, SQLAlchemyUnitOfWork)
    binder.bind(InvalidUserErrorCodeGenerator, InvalidUserErrorCodeGenerator)
    binder.bind(UserValidator, UserValidator)
