"""
This module holds request/response schemas for password related endpoints.
"""

from marshmallow import Schema, fields, validate, post_load

from useraccounts.common.error_message import AppErrorMessage
from useraccounts.common.constants import Constants
from useraccounts.schema._post_load_processor import hash_password
from useraccounts.schema._fields import password


class UpdatePasswordRequestSchema(Schema):
    user_id = fields.String(
        required=True,
        validate=validate.Length(min=1, error=AppErrorMessage.INVALID_USER_ID),
        error_messages={'required': AppErrorMessage.USER_ID_REQUIRED}
    )
    password = password

    @post_load
    def post_load_process(self, data, **kwargs):
        data[Constants.PASSWORD] = hash_password(data[Constants.PASSWORD])

        return data