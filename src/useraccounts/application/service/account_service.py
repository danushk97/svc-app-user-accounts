"""
This moudule acts as the service layer which helps to create, delete and update user account detail.
"""

from useraccounts.application.validator.account_validator import AccountValidator
from useraccounts.application.interfaces.unit_of_work import AbstractUnitOfWork
from useraccounts.domain.models import Account, Password
from useraccounts.schemas.account import AccountMetaSchema
from useraccounts.constants import Constants


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

    def create_account(self, create_account_schema: dict) -> AccountMetaSchema:
        """
        Creates user.

        Args:
            user_info (dict): Basic user information.

        Returns:
            (UserIdSchema): Contains the generated stable_id of the user.
        """
        account = Account(
            create_account_schema[Constants.EMAIL],
            create_account_schema[Constants.USERNAME],
            create_account_schema[Constants.ATTR]
        )
        account_stable_id = account.stable_id
        account.password = Password(
            create_account_schema[Constants.PASSWORD],
            created_by=account_stable_id
        )
        with self.unit_of_work as uow:
            import pdb; pdb.set_trace()
            AccountValidator.validate_for_create(
                account, uow.accounts
            )
            uow.accounts.add(account)
            uow.commit()
            
        return AccountMetaSchema(account_id=account_stable_id)
