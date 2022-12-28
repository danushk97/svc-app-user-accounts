"""
This module holds the exception classes.
"""

from http import HTTPStatus

from common.exception import AppException, InvalidParamsException

from useraccounts.constants import AppErrorMessage


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


class DuplicateEntryException(InvalidParamsException):
    def __init__(self, invalid_params: list) -> None:
        """
        Intansiates the class.
        """
        super().__init__(
            title=AppErrorMessage.REQUEST_PARAMS_DID_NOT_VALIDATE,
            detail='The data provided is not unique.',
            invalid_params=invalid_params,
            status=HTTPStatus.BAD_REQUEST
        )


# class InvalidCredetialException(AppException):
#     def __init__(self) -> None:
#         """
#         Intansiates the class.
#         """
#         super().__init__(
#             message=AppErrorMessage.INVALID_CREDENTIALS,
#             status_code=StatusCode.UNAUTHORIZED
#         )
