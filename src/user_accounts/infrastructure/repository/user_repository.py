"""
This modle holds the repository class for User.
"""

from sqlalchemy.exc import SQLAlchemyError
from apputils.error_handler import ErrorHandler

from user_accounts.infrastructure.repository.postgres_repository import PostgresRepository
from user_accounts.common.exception import PostgresRepositoryException
from user_accounts.domain.postgres_models.user import User


class UserRepository(PostgresRepository):
    """
    Contains helper functions to query user info.
    """

    def __init__(self, session):
        """
        Instantiates the class.
        """
        super().__init__(session)

    @ErrorHandler.handle_exception([SQLAlchemyError], PostgresRepositoryException)
    def get_user_by_attr_field(self, attr_field: str, attr_field_value: str) -> list:
        """
        Fetches user details based on attr fields.

        Args:
            attr_field (str): User ID.
            attr_field_value (str): str.

        Returns:
            result (list): List of users.

        Raises:
            PostgresRepositoryException: On SQLAlachemyError
        """
        result = self.session\
                     .query(User)\
                     .filter(User.attr[attr_field].astext \
                             == str(attr_field_value))\
                     .all()

        return result
