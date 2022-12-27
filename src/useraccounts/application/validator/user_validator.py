"""
This module holds the UserValidator class.
"""

from injector import inject

from useraccounts.application.error_code_generator.\
    invalid_user_error_code_generator import InvalidUserErrorCodeGenerator
from useraccounts.domain.entity.user import User
from useraccounts.infrastructure.sqlalchemy.repository.user_repository import UserRepository
from useraccounts.common.constants import Constants
from useraccounts.common.exception import DuplicateEntryException


class UserValidator:
    """
    Validates the user data.

    Attributes:
        error_code_generator (InvalidUserErrorCodeGenerator): Helps to generate error codes.
    """

    @inject
    def __init__(self, error_code_generator: InvalidUserErrorCodeGenerator):
        self.error_code_generator = error_code_generator

    def validate_is_unique_user(self, user: User, repository: UserRepository,
                                attr_keys=[Constants.EMAIL, Constants.DISPLAY_NAME]):
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
        errors = []

        for key in attr_keys:
            result = repository.get_user_by_attr_field(key, user.attr.get(key))
            if result:
                errors.extend(
                    [
                        self.error_code_generator.generate_duplicate_user_error_code(key)
                    ]
                )

        if errors:
            raise DuplicateEntryException(errors=errors)
