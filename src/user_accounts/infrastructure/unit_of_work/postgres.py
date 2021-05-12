"""
This module holds the unit of work class for sqlalchemy.
"""
import os

from user_accounts.infrastructure.unit_of_work.abstract_unit_of_work import \
    AbstractUnitOfWork
from user_accounts.infrastructure.repository.user_repository import \
    UserRepository
from user_accounts.infrastructure.repository.password_repository import \
    PasswordRepository
from user_accounts.infrastructure.sqlalchemy_session import \
    SQLAlchemySessionFactory


class PostgresUnitOfWork(AbstractUnitOfWork):
    """
    Handles and keeps track of all the transaction made with the database and
    also handles the database session.

    Attributes:
        session_factory (Session): SQLAlchemy session.
    """
    def __init__(self, session_factory=SQLAlchemySessionFactory,
                 db_connection_url=None):
        """
        Instantiates the class.
        """
        self.db_connection_url = db_connection_url or os.environ.get('DB_CONNECTION_URL')
        self.__session_factory = session_factory.get_instance(self.db_connection_url)

    def __enter__(self):
        """
        Gets executed when this instance of class is used with "with" statement.
        """
        self.__session = self.__session_factory()

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
        self.__session.commit()

    def flush(self) -> None:
        """
        Saves all the changes whcih was made during the current database
        session.
        """
        self.__session.flush()

    def rollback(self) -> None:
        """
        Discards all the changes whcih was made after the latest commit.
        """
        self.__session.rollback()

    def end_session(self) -> None:
        """
        Closes the current DB session.
        """
        self.__session_factory.remove()

    def user_repository(self) -> UserRepository:
        return UserRepository(self.__session)

    def password_repository(self) -> PasswordRepository:
        return PasswordRepository(self.__session)
