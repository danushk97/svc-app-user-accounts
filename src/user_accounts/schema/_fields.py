"""
This module holds the masrshmallow field configs.
"""


from marshmallow import fields, validate

from user_accounts.common.error_message import AppErrorMessage


password = fields.String(
    required=True,
    validate=validate.Length(min=8, max=40, error=AppErrorMessage.INVALID_PASSWORD_LENGTH),
    error_messages={
        'required': AppErrorMessage.PASSWORD_REQUIRED,
        'invalid': AppErrorMessage.INVALID_PASSWORD
    }
)
