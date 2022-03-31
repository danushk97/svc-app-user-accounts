"""
This modle holds the repository class for Password.
"""

from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import and_
from apputils.error_handler import ErrorHandler

from user_accounts.domain.value_object.password import Password
from user_accounts.infrastructure._repository.password_repository import AbstractPasswordRepository
from user_accounts.infrastructure.sqlalchemy.models.password import PasswordModel
from user_accounts.infrastructure.sqlalchemy.models.user import UserModel
from user_accounts.common.constants import Constants
from user_accounts.common.exception import RepositoryException


class PasswordRepository(AbstractPasswordRepository):
    """
    Contains helper functions to query user's password info.
    """

    def __init__(self, session):
        """
        Instantiates the class.
        """
        self._session = session

    @ErrorHandler.handle_exception([SQLAlchemyError], RepositoryException)
    def add(self, entity) -> None:
        self._session.add(entity)

    @ErrorHandler.handle_exception([SQLAlchemyError], RepositoryException)
    def update_password_by_user_id(self, user_id: str, password_hash: str) -> int:
        """
        Upates the password for the user_id.

        Args:
            user_id (str): User ID.
            password_hash (str): Encrypted password.

        Returns:
            row_affected (int): Number of rows affected.

        Raises:
            RepositoryException: On SQLAlachemyError
        """
        row_affected = self._session\
            .query(PasswordModel)\
            .filter(PasswordModel.user_id == user_id)\
            .update({Constants.HASH: password_hash})

        return row_affected
