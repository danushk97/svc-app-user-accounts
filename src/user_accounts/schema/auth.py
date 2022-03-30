from marshmallow import Schema, fields, validate

from user_accounts.common.error_codes.invalid_user_error_codes import AppErrorCodes
from user_accounts.schema._fields import password


class LoginRequestSchema(Schema):
    email = fields.String(
        required=True,
        validate=validate.Email(error=AppErrorCodes.INVALID_EMAIL),
        error_messages={'required': AppErrorCodes.EMAIL_REQUIRED}
    )
    password = password
