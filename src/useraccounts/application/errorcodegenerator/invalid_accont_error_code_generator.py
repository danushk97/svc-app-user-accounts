"""
This module holds the class which is responsible to validate request data.
"""

from useraccounts.constants import Constants, AppErrorMessage


class InvalidAccountErrorCodeGenerator:
    """
    Validates the data which comes along with the request.
    """
    @staticmethod
    def generate_duplicate_entry_error_code(duplicate_field: str) -> dict:
        """
        Returns a dict containing error info.

        Args:
            duplicate_field (str): A field name.

        Returns:
            (dict):
                field (str): Duplicate field name.
                message (str): An error message.
        """
        duplicate_field = str(duplicate_field).lower()
        error_messages = {
            Constants.EMAIL: AppErrorMessage.ACCOUNT_WITH_EMAIL_ID_ALREADY_EXISTS,
            Constants.USERNAME: AppErrorMessage.ACCOUNT_WITH_USERNAME_ALREADY_EXISTS,
            Constants.PHONE_NUMBER: AppErrorMessage.ACCOUNT_WITH_PHONE_NUMBER_ALREADY_EXISTS
        }

        return dict(
            field=duplicate_field,
            message=error_messages[duplicate_field]
        )
