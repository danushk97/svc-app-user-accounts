from http import HTTPStatus

from appscommon.exception import InvalidParamsException

from useraccounts.constants import AppErrorMessage


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
