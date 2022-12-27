"""
This modle holds the repository class for User.
"""

from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import and_
from apputils.error_handler import ErrorHandler

from useraccounts.common.exception import RepositoryException
from useraccounts.domain.value_object.password import Password
from useraccounts.domain.entity.user import User
from useraccounts.infrastructure._repository.user_repository import AbstractUserRepository
from useraccounts.infrastructure.sqlalchemy.models.user import UserModel
from useraccounts.infrastructure.sqlalchemy.models.password import PasswordModel


class UserRepository(AbstractUserRepository):
    """
    Contains helper functions to query user info.
    """

    def __init__(self, session):
        """
        Instantiates the class.
        """
        self._session = session

    @ErrorHandler.handle_exception([SQLAlchemyError], RepositoryException)
    def add(self, entity: User) -> None:
        user = entity.get_user_model()
        self._session.add(user)
        self._session.add_all(user.password)
        entity.stable_id = user.stable_id

        return entity

    @ErrorHandler.handle_exception([SQLAlchemyError], RepositoryException)
    def get_all_user_by_attr_field(self, attr_field: str, attr_field_value: str) -> list:
        """
        Fetches user details based on attr fields.

        Args:
            attr_field (str): User ID.
            attr_field_value (str): str.

        Returns:
            result (list): List of users.

        Raises:
            RepositoryException: On SQLAlachemyError
        """
        result = self._user_by_attr_query(attr_field, attr_field_value).all()

        return result

    @ErrorHandler.handle_exception([SQLAlchemyError], RepositoryException)
    def get_user_by_attr_field(self, attr_field: str, attr_field_value: str) -> User:
        data = self._user_by_attr_query(attr_field, attr_field_value, [UserModel, PasswordModel.hash])\
            .join(PasswordModel, and_(UserModel.stable_id == PasswordModel.user_id))\
            .one_or_none()

        if not data:
            return

        user_data, password_hash = data[0], data[1]
        user = User(
            stable_id=user_data.stable_id,
            attr=user_data.attr,
            password=Password(password_hash)
        )

        return user

    def _user_by_attr_query(self, attr_key, attr_value, query_models=[UserModel]):
        return self._session\
            .query(*query_models)\
            .filter(UserModel.attr[attr_key].astext == str(attr_value))
