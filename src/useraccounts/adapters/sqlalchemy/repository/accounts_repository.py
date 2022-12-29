from sqlalchemy.orm.query import Query
from sqlalchemy.orm.session import Session

from useraccounts.application.interfaces.accounts_repository import AbstractAccountsRepository
from useraccounts.domain.models import Account


class AccountsRepository(AbstractAccountsRepository):
    def __init__(self, session: Session) -> None:
        self._session = session
    
    def _select_account(self) -> Query:
        return self._session.query(Account)
    
    def get(self, id):
        return super().get(id)
    
    def list(self):
        return super().list()
        
    def get_by_username(self, username: str):
        return self._select_account().where(
            Account.username == username
        ).one_or_none()

    def get_by_email(self, email: str):
        return self._select_account().where(
            Account.email == email
        ).one_or_none()
