import traceback, sys
from sqlalchemy.exc import SQLAlchemyError
from apputils.error_handler import ErrorHandler

from user_accounts.infrastructure.repository.abstract_repository import \
    AbstractRepository
from user_accounts.common.exception import PostgresRepositoryException


class PostgresRepository(AbstractRepository):
    def __init__(self, session):
        self.session = session

    @ErrorHandler.handle_exception([SQLAlchemyError], PostgresRepositoryException)
    def add(self, entity) -> None:
        self.session.add(entity)
