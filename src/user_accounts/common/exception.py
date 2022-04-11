"""
This module holds the exception classes.
"""

from apputils.exception import AppException
from apputils.status_code import StatusCode

from user_accounts.common.error_message import AppErrorMessage


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


class DuplicateEntryException(AppException):
    def __init__(self, errors) -> None:
        """
        Intansiates the class.
        """
        super().__init__(
            message='The data provided is not unique.',
            errors=errors,
            status_code=StatusCode.BAD_REQUEST
        )


class InvalidCredetialException(AppException):
    def __init__(self) -> None:
        """
        Intansiates the class.
        """
        super().__init__(
            message=AppErrorMessage.INVALID_CREDENTIALS,
            status_code=StatusCode.UNAUTHORIZED
        )
