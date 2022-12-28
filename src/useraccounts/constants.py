"""
This module holds the constants.
"""

from common.exception.message import ErrorMessage
from common.readonly import ReadOnly


class Constants(ReadOnly):
    #string literals
    EMAIL = "email"
    HASH = "hash"
    DISPLAY_NAME = "display_name"
    PASSWORD = "password"
    SALT = "salt"
    PHONE_NUMBER = "phone_number"
    ERROR_CODE = "error_code"
    ERROR_DESCRIPTION = "error_description"
    STABLE_ID = "stable_id"
    ATTRIBUTES = "attributes"
    ATTR = "attr"
    USER_ID = "user_id"
    MINIMUM_HASH_ITERATION = "MINIMUM_HASH_ITERATION"
    MAXIMUM_HASH_ITERATION = "MAXIMUM_HASH_ITERATION"
    CREDENTIAL = "credential"
    DB_CONNECTION_STRING = "DB_CONNECTION_STRING"
    FIELD = "field"
    MESSAGE = "message"
    UNIT_OF_WORK = "unit_of_work"


class AppErrorMessage(ErrorMessage):
    INVALID_DISPLAY_NAME = "Please provide a valid display_name"
    INVALID_EMAIL = "Please provide a valid email."
    INVALID_PASSWORD = "Please provide a valid password"
    INVALID_PASSWORD_LENGTH = "password length must be between {min} and {max}."
    INVALID_USER_ID = "Please provide a valid user_id."
    ATTR_REQUIRED = "attr is required"
    USER_WITH_EMAIL_ID_ALREADY_EXISTS = "User with this email id already exists."
    USER_WITH_DISPLAY_NAME_ALREADY_EXISTS = "User with this display_name already exists."
    NO_USER_FOUND = "User not registered"
    EMAIL_REQUIRED = "email is required."
    USER_ID_REQUIRED = "user_id is required"
    DISPLAY_NAME_REQUIRED = "display_name is required."
    PASSWORD_REQUIRED = "password is required."
    INVALID_CREDENTIALS = "Invalid email or password"
