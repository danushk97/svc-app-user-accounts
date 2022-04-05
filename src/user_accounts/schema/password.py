"""
This module holds request/response schemas for password related endpoints.
"""

from marshmallow import Schema, fields, validate, post_load

from user_accounts.common.error_codes.invalid_user_error_codes import AppErrorCodes
from user_accounts.common.constants import Constants
from user_accounts.schema._post_load_processor import hash_password
from user_accounts.schema._fields import password


class UpdatePasswordRequestSchema(Schema):
    user_id = fields.String(
        required=True,
        validate=validate.Length(min=1, error=AppErrorCodes.INVALID_USER_ID),
        error_messages={'required': AppErrorCodes.USER_ID_REQUIRED}
    )
    password = password

    @post_load
    def post_load_process(self, data, **kwargs):
        data[Constants.PASSWORD] = hash_password(data[Constants.PASSWORD])

        return data