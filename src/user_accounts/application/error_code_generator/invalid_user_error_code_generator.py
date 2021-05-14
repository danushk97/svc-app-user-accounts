"""
This module holds the class which is responsible to validate request data.
"""

import logging

from user_accounts.common.constants import Constants
from apputils.status_code import StatusCode
from user_accounts.common.error_codes.invalid_user_error_codes import InvalidUserErrorCodes
from user_accounts.common.exception import InvalidPayloadException
from user_accounts.domain.user import User


class InvalidUserErrorCodeGenerator:
    """
    Validates the data which comes along with the request.

    Attributes:
        error_codes (list): Holds the list of error codes.
    """
    def generate_duplicate_user_error_code(self, duplicate_field: str):
        duplicate_field = str(duplicate_field).lower()

        if duplicate_field == Constants.EMAIL:
            return InvalidUserErrorCodes.USER_WITH_EMAIL_ID_ALREADY_EXISTS

        if duplicate_field == Constants.DISPLAY_NAME:
            return InvalidUserErrorCodes.USER_WITH_DISPLAY_NAME_ALREADY_EXISTS


    def generate_invalid_user_error_codes(self, user: User) -> list:
        """
        validates user payload.

        Args:
            payload (dict): User info

        Raises:
            InvalidPayloadException: If length of self.error_codes > 0
        """
        user_props = user.__dict__
        error_codes = []
        required_keys = [
            (Constants.EMAIL, InvalidUserErrorCodes.INVALID_EMAIL),
            (Constants.PASSWORD, InvalidUserErrorCodes.INVALID_PASSWORD),
            (Constants.DISPLAY_NAME, InvalidUserErrorCodes.INVALID_DISPLAY_NAME)
        ]
        self.__update_error_codes_for_empty_value(required_keys, user_props, error_codes)

        if hasattr(user, Constants.PASSWORD) and not user.password.is_valid():
            error_codes.append(InvalidUserErrorCodes.INVALID_PASSWORD_LENGTH)

        return error_codes

    def __update_error_codes_for_empty_value(self, keys: list, props: dict,
                                             error_codes: list) -> None:
        """
        Checks whether the list of keys are present in the payload.

        Args:
            payload (dict): User info.
        """
        for key, error_code in keys:
            value = props.get(f'_User__{key}')
            if not value:
                error_codes.append(error_code)
