from sqlalchemy.orm.query import Query
from sqlalchemy.orm.session import Session

from useraccounts.adapters.sqlalchemy.repository.exceptions import sql_error_handler
from useraccounts.application.interfaces.accounts_repository import AbstractAccountsRepository
from useraccounts.domain.models import Account


class AccountsRepository(AbstractAccountsRepository):
    def __init__(self, session: Session) -> None:
        self._session: Session = session

    def _select_account(self) -> Query:
        return self._session.query(Account)

    def get(self, id):
        return super().get(id)

    def list(self):
        return super().list()

    @sql_error_handler
    def get_by_username(self, username: str):
        return self._select_account().where(
            Account.username == username,
            Account.is_active == True
        ).one_or_none()

    @sql_error_handler
    def get_by_email(self, email: str):
        return self._select_account().where(
            Account.email == email,
            Account.is_active == True
        ).one_or_none()

    @sql_error_handler
    def get_by_phone_number(self, phone_number: int):
        return self._select_account().where(
            Account.phone_number == phone_number,
            Account.is_active == True
        ).one_or_none()
    