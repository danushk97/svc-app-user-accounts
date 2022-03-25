"""
This module holds the UserValidator class.
"""

from injector import inject

from user_accounts.application.error_code_generator.\
    invalid_user_error_code_generator import InvalidUserErrorCodeGenerator
from user_accounts.domain.entity.user import User
from user_accounts.infrastructure.sqlalchemy.repository.user_repository import UserRepository
from user_accounts.common.constants import Constants
from user_accounts.common.exception import InvalidUserException


class UserValidator:
    """
    Validates the user data.

    Attributes:
        error_code_generator (InvalidUserErrorCodeGenerator): Helps to generate
        error codes.
    """

    @inject
    def __init__(self, error_code_generator: InvalidUserErrorCodeGenerator):
        self.error_code_generator = error_code_generator

    def validate_is_unique_user(self, user: User,
                                repository: UserRepository,
                                attr_keys=[Constants.EMAIL,
                                           Constants.DISPLAY_NAME]):
        """
        Validates whether the user is unique.

        Args:
            user (User): User object that needs to be validated.
            repository (UserRepository): repository class which helps to
            communicate with DB.
            attr_keys (list): List of keys that should be considered for
            validation.

        Raises:
            InvalidUserException: On duplicate entry.
        """
        error_codes = []

        for key in attr_keys:
            result = repository.get_user_by_attr_field(key, getattr(user, key))
            if result:
                error_codes.extend([self.error_code_generator\
                           .generate_duplicate_user_error_code(key)])

        if error_codes:
            raise InvalidUserException(error_codes=error_codes)

    def validate_user(self, user: User) -> None:
        """
        Validates whether the user object is valid.

        Args:
            user (User): Object that needs to be validated.

        Raises:
            InvalidUserException: if the user is invalid
        """
        if not user.is_valid():
            error_codes = self.error_code_generator\
                              .generate_invalid_user_error_codes(user)
            raise InvalidUserException(error_codes=error_codes)
