"""
This module holds the unit of work class for sqlalchemy.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session, Session

from useraccounts.config import Config
from useraccounts.adapters.sqlalchemy.repository import UsersRepository
from useraccounts.application.interfaces.unit_of_work import AbstractUnitOfWork


engine = create_engine(Config.DB_CONNECTION_STRING)
session = scoped_session(sessionmaker(bind=engine))


class SQLAlchemyUnitOfWork(AbstractUnitOfWork):
    """
    Handles and keeps track of all the transaction made with the database and
    also handles the database session.

    Attributes:
        session_factory (Session): SQLAlchemy session.
    """
    def __init__(self, session_factory=session):
        """
        Instantiates the class.
        """
        self._session_factory = session_factory
        self._users = None

    def __enter__(self):
        """
        Gets executed when this instance of class is used with "with" statement.
        """
        self._session: Session = self._session_factory()

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

    @property
    def users(self) -> UsersRepository:
        if not self._users:
            self._users = UsersRepository(self._session)
        
        return self._users
