"""
This module holds a class which defines invalid user error codes.
"""

from apputils.error_codes.error_codes import ErrorCodes


class InvalidUserErrorCodes(ErrorCodes):
    """
    Holds the error codes related to invalid user.
    """
    INTERNAL_SERVER_ERROR = (5000, 'Internal server error')
    INVALID_DISPLAY_NAME = (4001, 'Please provide a valid display_name')
    INVALID_EMAIL = (4002, 'Please provide a valid email')
    INVALID_PASSWORD = (4006, 'Please provide a valid password')
    INVALID_PASSWORD_LENGTH = (4007, 'password length must be between 8 and 40')
    USER_WITH_EMAIL_ID_ALREADY_EXISTS = (4008, 'User with this email id aleady exists')
    USER_WITH_DISPLAY_NAME_ALREADY_EXISTS = (4009, 'User with this display_name aleady exists')
    INVALID_USER_ID = (4011, 'Please provide a valid user_id')
    NO_USER_FOUND = (4012, 'User not registered')
