"""
This moudule acts as the service layer which helps to update user password.
"""

import jwt
from injector import inject
from apputils.error_handler import ErrorHandler
from apputils.status_code import StatusCode

from user_accounts.infrastructure.sqlalchemy.models import password
from user_accounts.infrastructure.sqlalchemy.unit_of_work import SQLAlchemyUnitOfWork
from user_accounts.application._service import Service
from user_accounts.common.constants import Constants
from user_accounts.common.exception import NoUserFoundException, InvalidCredetialException, PasswordServiceException
from user_accounts.common.exception import RepositoryException
from user_accounts.common.error_codes.invalid_user_error_codes import AppErrorCodes
from user_accounts.domain.value_object.password import Password


class AuthService(Service):
    """
    Authentication service layer.

    Attributes:
        unit_of_work (SQLAlchemyUnitOfWork): Helps communicating with the database.
    """
    @inject
    def __init__(self, unit_of_work: SQLAlchemyUnitOfWork):
        """
        Instantiates the class.
        """
        self.unit_of_work = unit_of_work

    @ErrorHandler.handle_exception([RepositoryException], PasswordServiceException)
    def login(self, login_data: dict) -> None:
        """
        Validates credential and returns a JWT if the credential is valid.

        Args:
            login_data (dict):
                email (str): User email id.
                password (str): Password.

        Returns:
            jwt_token ()
        """
        user = self.initiate_db_transaction(self._get_user_by_email, login_data[Constants.EMAIL])

        if not Password.do_match(login_data[Constants.PASSWORD].encode(), user.password.hash):
            raise InvalidCredetialException()

        # TODO: Need to move secret to env_var and to update the payload
        jwt_token = jwt.encode({Constants.USER_ID: user.stable_id}, 'secret')

        return jwt_token

    def _get_user_by_email(self, unit_of_work: SQLAlchemyUnitOfWork, email: str) -> tuple:
        """
        Helps to get password hash of the under the requested user_id.

        Args:
            unit_of_work (SQLAlchemyUnitOfWork)
            email (str): User email id.

        Returns:
            user_password (tuple): Contains the user_id at place 0 and
            password_hash at place 1

        Raises:
            PasswordServiceException: On no data found.
        """
        repository = unit_of_work.user_repository()
        user = repository.get_user_by_attr_field(Constants.EMAIL, email)

        if not user:
            raise NoUserFoundException([
                AppErrorCodes.NO_USER_FOUND
            ], StatusCode.BAD_REQUEST)

        return user
