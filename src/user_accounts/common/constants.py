"""
This module holds the constants.
"""

from apputils.read_only import ReadOnly


class Constants(ReadOnly):
    #string literals
    EMAIL = 'email'
    HASH = 'hash'
    DISPLAY_NAME = 'display_name'
    PASSWORD = 'password'
    SALT = 'salt'
    PHONE_NUMBER = 'phone_number'
    ERROR_CODE = 'error_code'
    ERROR_DESCRIPTION = 'error_description'
    STABLE_ID = 'stable_id'
    ATTRIBUTES = 'attributes'
    ATTR = 'attr'
    USER_ID = 'user_id'
    MINIMUM_HASH_ITERATION = 'MINIMUM_HASH_ITERATION'
    MAXIMUM_HASH_ITERATION = 'MAXIMUM_HASH_ITERATION'
    CREDENTIAL = 'credential'
    DB_CONNECTION_STRING = 'DB_CONNECTION_STRING'
