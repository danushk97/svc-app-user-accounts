from marshmallow import fields, validate

from user_accounts.common.error_codes.invalid_user_error_codes import AppErrorCodes


password = fields.String(
        required=True,
        validate=validate.Length(min=8, max=40, error=AppErrorCodes.INVALID_PASSWORD_LENGTH),
        error_messages={
            'required': AppErrorCodes.PASSWORD_REQUIRED,
            'invalid': AppErrorCodes.INVALID_PASSWORD
        }
    )