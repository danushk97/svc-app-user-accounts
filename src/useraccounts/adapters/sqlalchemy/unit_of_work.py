"""
This module holds the unit of work class for sqlalchemy.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from appscommon.db.adapters.unit_of_work import UnitOfWork

from useraccounts.config import config
from useraccounts.constants import Constants
from useraccounts.adapters.sqlalchemy.repository import AccountsRepository


class SQLAlchemyUnitOfWork(UnitOfWork):
    """
    Handles and keeps track of all the transaction made with the database and
    also handles the database session.

    Attributes:
        session_factory (Session): SQLAlchemy session.
    """
    _engine = create_engine(config[Constants.DB_CONNECTION_STRING])
    
    def __init__(self, session_factory: scoped_session = None):
        """
        Instantiates the class.
        """
        super().__init__(
            session_factory or self._get_session_maker(),
        )

    def __enter__(self):
        super().__enter__()  #  initializes session in self._session
        self.accounts = AccountsRepository(self._session)

        return self

    def _get_session_maker(self) -> scoped_session:
        return scoped_session(sessionmaker(bind=self._engine))
