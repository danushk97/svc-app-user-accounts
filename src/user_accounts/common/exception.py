"""
This module holds the exception classes.
"""

from apputils.exception import AppException
from apputils.status_code import StatusCode

from user_accounts.common.error_codes.auth_error_code import AuthErrorCodes


class InvalidPayloadException(AppException):
    pass


class UserServiceException(AppException):
    pass


class RepositoryException(AppException):
    pass


class PasswordServiceException(AppException):
    pass


class NoUserFoundException(AppException):
    pass


class InvalidRequestException(AppException):
    pass


class InvalidPasswordException(AppException):
    pass


class InvalidUserException(AppException):
    def __init__(self, error_codes:list=None,
                 status_code:int=StatusCode.BAD_REQUEST) -> None:
        """
        Intansiates the class.
        """
        super().__init__(error_codes=error_codes, status_code=status_code)


class InvalidCredetialException(AppException):
    def __init__(self, error_codes: list=[AuthErrorCodes.INVALID_CREDENTIALS],
                 status_code: int=StatusCode.UNAUTHORIZED) -> None:
        """
        Intansiates the class.
        """
        super().__init__(error_codes=error_codes, status_code=status_code)
