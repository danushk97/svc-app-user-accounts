"""
This module holds request/response schemas for auth related endpoints.
"""

from marshmallow import Schema, fields, validate

from user_accounts.common.error_message import AppErrorMessage
from user_accounts.schema._fields import password


class LoginRequestSchema(Schema):
    email = fields.String(
        required=True,
        validate=validate.Email(error=AppErrorMessage.INVALID_EMAIL),
        error_messages={'required': AppErrorMessage.EMAIL_REQUIRED}
    )
    password = password
