"""
This module holds the class which is responsible to validate request data.
"""

from user_accounts.common.constants import Constants
from user_accounts.common.error_codes.invalid_user_error_codes import \
    InvalidUserErrorCodes
from user_accounts.domain.entity.user import User


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
        error_codes = []
        required_values = [
            (user.email, InvalidUserErrorCodes.INVALID_EMAIL),
            (user.password, InvalidUserErrorCodes.INVALID_PASSWORD),
            (user.display_name, InvalidUserErrorCodes.INVALID_DISPLAY_NAME)
        ]
        self.__update_error_codes_for_empty_value(required_values, error_codes)

        if hasattr(user, Constants.PASSWORD) and not user.password.is_valid():
            error_codes.append(InvalidUserErrorCodes.INVALID_PASSWORD_LENGTH)

        if user.email and not user.isvalid_email():
            error_codes.append(InvalidUserErrorCodes.INVALID_EMAIL)

        return error_codes

    def __update_error_codes_for_empty_value(self, values: list,
                                             error_codes: list) -> None:
        """
        Checks whether the list of keys are present in the payload.

        Args:
            payload (dict): User info.
        """
        for value, error_code in values:
            if not value:
                error_codes.append(error_code)
