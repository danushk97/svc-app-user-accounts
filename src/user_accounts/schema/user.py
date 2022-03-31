"""
This module holds request/response schemas for user related endpoints.
"""

from marshmallow import Schema, fields, validate, post_load

from user_accounts.common.constants import Constants
from user_accounts.common.error_codes.invalid_user_error_codes import AppErrorCodes
from user_accounts.schema._post_load_processor import hash_password
from user_accounts.schema._fields import password


class UserAttrSchema(Schema):
    email = fields.String(
        required=True,
        validate=validate.Email(error=AppErrorCodes.INVALID_EMAIL),
        error_messages={'required': AppErrorCodes.EMAIL_REQUIRED}
    )
    display_name = fields.String(
        required=True,
        validate=validate.Length(min=1, error=AppErrorCodes.INVALID_DISPLAY_NAME),
        error_messages={'required': AppErrorCodes.DISPLAY_NAME_REQUIRED}
    )


class CreateUserRequestSchema(Schema):
    attr = fields.Nested(
        UserAttrSchema,
        required=True,
        error_messages={'required': AppErrorCodes.ATTR_REQUIRED}
    )
    password = password

    @post_load
    def post_load_process(self, data, **kwargs):
        data[Constants.PASSWORD] = hash_password(data[Constants.PASSWORD])

        return data


class CreateUserResponseSchema(Schema):
    user_id = fields.String(required=True)
