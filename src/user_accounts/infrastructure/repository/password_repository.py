"""
This modle holds the repository class for Password.
"""

from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import and_

from user_accounts.infrastructure.repository.postgres_repository import \
    PostgresRepository
from user_accounts.domain.postgres_models.password import Password
from user_accounts.domain.postgres_models.user import User
from user_accounts.common.constants import Constants
from user_accounts.common.exception import PostgresRepositoryException
from apputils.error_handler import ErrorHandler


class PasswordRepository(PostgresRepository):
    """
    Contains helper functions to query user's password info.
    """

    def __init__(self, session):
        """
        Instantiates the class.
        """
        super().__init__(session)

    @ErrorHandler.handle_exception([SQLAlchemyError], PostgresRepositoryException)
    def update_password_by_user_id(self, user_id: str, password_hash: str) -> int:
        """
        Upates the password for the user_id.

        Args:
            user_id (str): User ID.
            password_hash (str): Encrypted password.

        Returns:
            row_affected (int): Number of rows affected.

        Raises:
            PostgresRepositoryException: On SQLAlachemyError
        """
        attr = {Constants.CREDENTIAL: password_hash}
        row_affected = self.session\
                            .query(Password)\
                            .filter(Password.user_id == user_id)\
                            .update({Constants.ATTR: attr})

        return row_affected

    @ErrorHandler.handle_exception([SQLAlchemyError], PostgresRepositoryException)
    def get_password_hash_by_email(self, email: str) -> str:
        """
        Fetches password hash for the user_id.

        Args:
            email (str): User email id.

        Returns:
            password_hash (str): Password Hash.

        Raises:
            PostgresRepositoryException: On SQLAlachemyError
        """
        password = self.session\
                       .query(Password)\
                       .join(User, and_(Password.user_id == User.stable_id))\
                       .filter(User.attr[Constants.EMAIL].astext == email)\
                       .one()

        if password:
            password_hash = password.attr[Constants.CREDENTIAL]
            return password_hash
