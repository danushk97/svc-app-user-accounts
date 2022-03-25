"""
This module holds the class which defines the sqlalchemy session.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session


class SQLAlchemySessionFactory:
    """
    Creates Database engine and provides session factory which later can be
    initiated in order to communicate with Database.

    Attributes:
        db_connection_url (str): Database connection url.
        engine (Engine): Database engine
        session_factory (Session): Session Factory.
    """
    _instance = None

    def __init__(self, db_connection_url: str):
        """
        Instantiates the class.
        """
        if not SQLAlchemySessionFactory._instance:
            engine = create_engine(db_connection_url)
            self._session_factory = scoped_session(sessionmaker(bind=engine))
            SQLAlchemySessionFactory._instance = self
        else:
            raise Exception('You cannot instantiate SQLAlchemySession twice!')

    def __call__(self):
        return self._session_factory()

    def remove(self):
        self._session_factory.remove()

    @staticmethod
    def get_instance(db_connection_url: str):
        """
        Returns the instance of SQLAlchemySession.

        Args:
            db_connection_url (str): Database connection url.

        Returns:
            SQLAlchemySession
        """
        if SQLAlchemySessionFactory._instance:
            return SQLAlchemySessionFactory._instance

        return SQLAlchemySessionFactory(db_connection_url)
