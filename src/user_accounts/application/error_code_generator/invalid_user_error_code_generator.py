"""
This module holds the class which is responsible to validate request data.
"""

from user_accounts.common.constants import Constants
from user_accounts.common.error_message import AppErrorMessage


class InvalidUserErrorCodeGenerator:
    """
    Validates the data which comes along with the request.

    Attributes:
        error_codes (list): Holds the list of error codes.
    """
    def generate_duplicate_user_error_code(self, duplicate_field: str):
        duplicate_field = str(duplicate_field).lower()

        if duplicate_field == Constants.EMAIL:
            return {
                Constants.FIELD: duplicate_field,
                Constants.MESSAGE: AppErrorMessage.USER_WITH_EMAIL_ID_ALREADY_EXISTS
            }

        if duplicate_field == Constants.DISPLAY_NAME:
            return {
                Constants.FIELD: duplicate_field,
                Constants.MESSAGE: AppErrorMessage.USER_WITH_DISPLAY_NAME_ALREADY_EXISTS
            }
