"""
This moudule acts as the service layer which helps to create, delete and update user account detail.
"""

from appscommon.db.interfaces.unit_of_work import AbstractUnitOfWork

from useraccounts.application.validator.account_validator import AccountValidator
from useraccounts.domain.models import Account
from useraccounts.schemas.account import CreateAccountRequestSchema


class AccountService:
    """
    Holds business usecase/logic which are related to user creation/updation/deletion.

    Attributes:
        unit_of_work (AbstractUnitOfWork): Helps communicating with the postgres database.
    """
    def __init__(self, unit_of_work: AbstractUnitOfWork):
        """
        Instantiates the class.
        """
        self.unit_of_work = unit_of_work

    def create_account(self, create_account_schema: CreateAccountRequestSchema) -> None:
        """
        Creates user account.

        Args:
            create_account_schema (CreateAccountRequestSchema): Basic user information.
        """
        account = Account.from_create_account_schema(create_account_schema)
        with self.unit_of_work as uow:
            AccountValidator.validate_for_create(
                account, uow.accounts
            )
            uow.accounts.add(account)
            uow.commit()
