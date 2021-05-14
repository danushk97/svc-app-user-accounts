"""
This moudule acts as the service layer which helps to update user password.
"""

from injector import inject
from apputils.error_handler import ErrorHandler
from apputils.status_code import StatusCode

from user_accounts.infrastructure.unit_of_work.postgres import \
    PostgresUnitOfWork
from user_accounts.application.base_service import BaseService
from user_accounts.common.constants import Constants
from user_accounts.common.exception import PasswordServiceException
from user_accounts.common.exception import InvalidRequestException
from user_accounts.common.exception import InvalidPasswordException
from user_accounts.common.exception import InvalidCredetialException
from user_accounts.common.exception import PostgresRepositoryException
from user_accounts.common.error_codes.invalid_user_error_codes import \
    InvalidUserErrorCodes
from user_accounts.domain.password import Password
from user_accounts.domain.postgres_models.password import Password as PasswordModel


class PasswordService(BaseService):
    """
    Holds business usecase/logic which are related to password creation/updation.

    Attributes:
        postgres_unit_of_work (PostgresUnitOfWork): Helps communicating with
        the postgres database.
    """
    @inject
    def __init__(self, unit_of_work: PostgresUnitOfWork):
        """
        Instantiates the class.
        """
        self.unit_of_work = unit_of_work

    @ErrorHandler.handle_exception([PostgresRepositoryException],
                                    PasswordServiceException)
    def update_password(self, user_id: str, password: str) -> dict:
        """
        Update Password.

        Args:
            update_info (dict): Should hold the password and user_id.
        """
        self.__check_user_id(user_id)
        password = self.__get_password_object(password)

        if not password.is_valid():
            raise InvalidPasswordException([
                InvalidUserErrorCodes.INVALID_PASSWORD_LENGTH
            ])

        self.initiate_db_transaction(self.__update_password, user_id,
                                     password.password_hash.decode('utf-8'))

    @ErrorHandler.handle_exception([PostgresRepositoryException],
                                    PasswordServiceException)
    def validate_credential(self, email: str, password: str) -> None:
        """
        Validates credential.

        Args:
            email (str): User email id.
            password (str): Password.
        """
        self.__check_email(email)
        credential = self.initiate_db_transaction(self.__get_password_hash,
                                                  email)
        Password.validate_password(password.encode(), credential.encode())

    def __get_password_hash(self, unit_of_work: PostgresUnitOfWork,
                            email: str) -> str:
        """
        Helps to get password hash of the under the requested user_id.

        Args:
            unit_of_work (PostgresUnitOfWork)
            email (str): User email id.

        Returns:
            password_hash (str): Hashed password string.

        Raises:
            PasswordServiceException: On no data found.
        """
        repository = unit_of_work.password_repository()
        password_hash = repository.get_password_hash_by_email(email)

        if not password_hash:
            raise PasswordServiceException([
                InvalidUserErrorCodes.NO_USER_FOUND
            ], StatusCode.BAD_REQUEST)

        return password_hash


    def __update_password(self, unit_of_work: PostgresUnitOfWork,
                          user_id: str, password_hash: str):
        """
        Helps to update password.

        Args:
            unit_of_work (PostgresUnitOfWork): An interface to communicate with
            Database.
            user_id (str): User ID.
            password_hash (str): Hashed password string.

        Raises:
            PasswordServiceException: On no record got updated.
        """
        repository = unit_of_work.password_repository()
        affected_rows = repository.update_password_by_user_id(user_id,
                                                              password_hash)
        if not affected_rows:
            raise PasswordServiceException([
                InvalidUserErrorCodes.NO_USER_FOUND
            ], StatusCode.BAD_REQUEST)

        unit_of_work.commit()

    def __get_password_object(self, password: str) -> Password:
        return Password(password)

    def __check_email(self, email: str):
        if not email:
            raise InvalidRequestException([
                InvalidUserErrorCodes.INVALID_EMAIL
            ])

    def __check_user_id(self, user_id: str):
        if not user_id:
            raise InvalidRequestException([
                InvalidUserErrorCodes.INVALID_USER_ID
            ])
