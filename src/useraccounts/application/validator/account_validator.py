"""
This module holds the UserValidator class.
"""

from useraccounts.application.errorcodegenerator.invalid_accont_error_code_generator import \
    InvalidAccountErrorCodeGenerator
from useraccounts.application.interfaces.accounts_repository import AbstractAccountsRepository
from useraccounts.application.validator.exception import DuplicateEntryException
from useraccounts.constants import Constants
from useraccounts.domain.models import Account


class AccountValidator:
    """
    Validates the user data.
    """
    @staticmethod
    def validate_for_create(
        account: Account,
        accounts_repo: AbstractAccountsRepository,
        fields: list = [Constants.EMAIL, Constants.USERNAME]
    ):
        """
        Validates whether the user is unique.

        Args:
            account (Account): Account instance.
            accounts_repo (AbstractAccountsRepository): repository class which helps to communicate with DB.
            fields (list): List of keys that should be considered for validation.

        Raises:
            DuplicateEntryException: On duplicate entry.
        """
        invalid_params = []
        for field in fields:
            method = getattr(accounts_repo, f'get_by_{field}')
            arg = getattr(account, field)
            data = method(arg)
            if data:
                invalid_params.append(
                    InvalidAccountErrorCodeGenerator.generate_duplicate_entry_error_code(field)
                )

        if invalid_params:
            raise DuplicateEntryException(invalid_params=invalid_params)
