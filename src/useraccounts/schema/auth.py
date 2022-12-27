"""
This module holds request/response schemas for auth related endpoints.
"""

from marshmallow import Schema, fields, validate

from useraccounts.common.error_message import AppErrorMessage
from useraccounts.schema._fields import password


class LoginRequestSchema(Schema):
    email = fields.String(
        required=True,
        validate=validate.Email(error=AppErrorMessage.INVALID_EMAIL),
        error_messages={'required': AppErrorMessage.EMAIL_REQUIRED}
    )
    password = password
