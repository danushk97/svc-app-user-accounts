"""
This module holds the unit of work class for sqlalchemy.
"""
from user_accounts.config import Config

from user_accounts.infrastructure._unit_of_work import AbstractUnitOfWork
from user_accounts.infrastructure.sqlalchemy.repository.user_repository import UserRepository
from user_accounts.infrastructure.sqlalchemy.repository.password_repository import PasswordRepository
from user_accounts.infrastructure.sqlalchemy.session import SQLAlchemySessionFactory


class SQLAlchemyUnitOfWork(AbstractUnitOfWork):
    """
    Handles and keeps track of all the transaction made with the database and
    also handles the database session.

    Attributes:
        session_factory (Session): SQLAlchemy session.
    """
    def __init__(self, session_factory=SQLAlchemySessionFactory, db_connection_url=None):
        """
        Instantiates the class.
        """
        self.db_connection_url = db_connection_url or Config.DB_CONNECTION_STRING
        self._session_factory = session_factory.get_instance(self.db_connection_url)

    def __enter__(self):
        """
        Gets executed when this instance of class is used with "with" statement.
        """
        self._session = self._session_factory()

        return self

    def __exit__(self, *args) -> None:
        """
        Gets executed after the code within the "with" statement gets executed.
        """
        self.rollback()
        self.end_session()

    def commit(self) -> None:
        """
        Saves all the changes whcih was made during the current database
        session.
        """
        self._session.commit()

    def flush(self) -> None:
        """
        Saves all the changes whcih was made during the current database
        session.
        """
        self._session.flush()

    def rollback(self) -> None:
        """
        Discards all the changes whcih was made after the latest commit.
        """
        self._session.rollback()

    def end_session(self) -> None:
        """
        Closes the current DB session.
        """
        self._session_factory.remove()

    def user_repository(self) -> UserRepository:
        return UserRepository(self._session)

    def password_repository(self) -> PasswordRepository:
        return PasswordRepository(self._session)
