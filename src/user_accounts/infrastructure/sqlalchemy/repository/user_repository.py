"""
This modle holds the repository class for User.
"""

from sqlalchemy.exc import SQLAlchemyError
from apputils.error_handler import ErrorHandler

from user_accounts.infrastructure._repository.user_repository import AbstractUserRepository
from user_accounts.common.exception import RepositoryException
from user_accounts.infrastructure.sqlalchemy.models.user import UserModel


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
    def add(self, entity) -> None:
        self.session.add(entity)

    @ErrorHandler.handle_exception([SQLAlchemyError], RepositoryException)
    def get_user_by_attr_field(self, attr_field: str, attr_field_value: str) -> list:
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
        result = self._session\
                     .query(UserModel)\
                     .filter(UserModel.attr[attr_field].astext \
                             == str(attr_field_value))\
                     .all()

        return result
