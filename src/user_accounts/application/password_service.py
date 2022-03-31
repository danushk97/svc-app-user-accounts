"""
This moudule acts as the service layer which helps to update user password.
"""

from injector import inject
from apputils.error_handler import ErrorHandler
from apputils.status_code import StatusCode

from user_accounts.infrastructure.sqlalchemy.unit_of_work import SQLAlchemyUnitOfWork
from user_accounts.application._service import Service
from user_accounts.common.exception import PasswordServiceException
from user_accounts.common.exception import RepositoryException
from user_accounts.common.error_codes.invalid_user_error_codes import AppErrorCodes
from user_accounts.domain.value_object.password import Password


class PasswordService(Service):
    """
    Holds business usecase/logic which are related to password creation/updation.

    Attributes:
        unit_of_work (SQLAlchemyUnitOfWork): Helps communicating with
        the postgres database.
    """
    @inject
    def __init__(self, unit_of_work: SQLAlchemyUnitOfWork):
        """
        Instantiates the class.
        """
        self.unit_of_work = unit_of_work

    @ErrorHandler.handle_exception([RepositoryException], PasswordServiceException)
    def update_password(self, user_id: str, password: str) -> dict:
        """
        Update Password.

        Args:
            update_info (dict): Should hold the password and user_id.
        """
        password = self._get_password_object(password)

        self.initiate_db_transaction(
            self._update_password, user_id, password.hash
        )

    def _update_password(self, unit_of_work: SQLAlchemyUnitOfWork, user_id: str, password_hash: str):
        """
        Helps to update password.

        Args:
            unit_of_work (SQLAlchemyUnitOfWork): An interface to communicate with
            Database.
            user_id (str): User ID.
            password_hash (str): Hashed password string.

        Raises:
            PasswordServiceException: On no record got updated.
        """
        repository = unit_of_work.password_repository()
        affected_rows = repository.update_password_by_user_id(user_id, password_hash)

        if not affected_rows:
            raise PasswordServiceException([
                AppErrorCodes.NO_USER_FOUND
            ], StatusCode.BAD_REQUEST)

        unit_of_work.commit()

    def _get_password_object(self, password: str) -> Password:
        return Password(password)
