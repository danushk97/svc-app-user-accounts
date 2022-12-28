from useraccounts.application.interfaces.users_repository import AbstractUsersRepository
from useraccounts.domain.models import User

from sqlalchemy.orm.session import Session


class UsersRepository(AbstractUsersRepository):
    def __init__(self, session: Session) -> None:
        self._session = session
    
    def add(self, user_account: User):
        self._session.add(user_account)
    
    def get_by_stable_id(self, stable_id: str) -> User:
        return self._session.query(
            User
        ).where(
            User.stable_id == stable_id
        ).one_or_none()
    
    def get_by_attr_field(self, field: str, value: str) -> User:
        return self._session.query(
            User
        ).where(
            User.attr.op('->>')(field) == value
        ).one_or_none()
    