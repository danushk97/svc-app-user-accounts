from marshmallow import Schema, fields, validate

from user_accounts.common.error_codes.invalid_user_error_codes import AppErrorCodes
from user_accounts.schema._fields import password


class UpdatePasswordRequestSchema(Schema):
    user_id = fields.String(
        required=True,
        validate=validate.Length(min=1, error=AppErrorCodes.INVALID_USER_ID),
        error_messages={'required': AppErrorCodes.USER_ID_REQUIRED}
    )
    password = password
