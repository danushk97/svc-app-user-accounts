"""
This module holds the UserValidator class.
"""

from useraccounts.application.error_code_generator.invalid_user_error_code_generator import \
    InvalidUserErrorCodeGenerator
from useraccounts.application.interfaces.users_repository import AbstractUsersRepository
from useraccounts.common.exception import DuplicateEntryException
from useraccounts.constants import Constants
from useraccounts.domain.models import User


class UserValidator:
    """
    Validates the user data.
    """
    @staticmethod
    def validate_for_create( 
        user: User, 
        users_repo: AbstractUsersRepository, 
        attr_keys: list = [Constants.EMAIL, Constants.DISPLAY_NAME]
    ):
        """
        Validates whether the user is unique.

        Args:
            user (UserAccount): User object that needs to be validated.
            repository (AbstractUserAccountsRepository): repository class which helps to communicate with DB.
            attr_keys (list): List of keys that should be considered for validation.

        Raises:
            DuplicateEntryException: On duplicate entry.
        """
        invalid_params = []
        for key in attr_keys:
            data = users_repo.get_by_attr_field(key, user.attr.get(key))
            if data:
                invalid_params.append(
                    InvalidUserErrorCodeGenerator.generate_duplicate_entry_error_code(key)
                )
        if invalid_params:
            raise DuplicateEntryException(invalid_params=invalid_params)
