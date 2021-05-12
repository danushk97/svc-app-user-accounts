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
    __instance = None

    def __init__(self, db_connection_url: str):
        """
        Instantiates the class.
        """
        if not SQLAlchemySessionFactory.__instance:
            engine = create_engine(db_connection_url)
            self.__session_factory = scoped_session(sessionmaker(bind=engine))
            SQLAlchemySessionFactory.__instance = self
        else:
            raise Exception('You cannot instantiate SQLAlchemySession twice!')

    def __call__(self):
        return self.__session_factory()

    def remove(self):
        self.__session_factory.remove()

    @staticmethod
    def get_instance(db_connection_url: str):
        """
        Returns the instance of SQLAlchemySession.

        Args:
            db_connection_url (str): Database connection url.

        Returns:
            SQLAlchemySession
        """
        if SQLAlchemySessionFactory.__instance:
            return SQLAlchemySessionFactory.__instance

        return SQLAlchemySessionFactory(db_connection_url)
