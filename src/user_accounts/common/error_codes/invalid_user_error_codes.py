"""
This module holds a class which defines invalid user error codes.
"""

from apputils.error_codes.error_codes import ErrorCodes


class AppErrorCodes(ErrorCodes):
    """
    Holds the error codes related to invalid user.
    """

    INTERNAL_SERVER_ERROR = 'Internal server error'
    INVALID_DISPLAY_NAME = 'Please provide a valid display_name'
    INVALID_EMAIL = 'Please provide a valid email'
    INVALID_PASSWORD = 'Please provide a valid password'
    INVALID_PASSWORD_LENGTH = 'password length must be between {min} and {max}'
    INVALID_USER_ID = 'Please provide a valid user_id'
    ATTR_REQUIRED = 'attr is required'
    USER_WITH_EMAIL_ID_ALREADY_EXISTS = 'User with this email id aleady exists'
    USER_WITH_DISPLAY_NAME_ALREADY_EXISTS = 'User with this display_name aleady exists'
    NO_USER_FOUND = 'User not registered'
    EMAIL_REQUIRED = 'email is required'
    USER_ID_REQUIRED = 'user_id is required'
    DISPLAY_NAME_REQUIRED = 'display_name is required'
    PASSWORD_REQUIRED = 'password is required'
