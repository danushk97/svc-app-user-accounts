"""
This module holds a class which defines invalid user error codes.
"""

from apputils.error_message import ErrorMessage


class AppErrorMessage(ErrorMessage):
    INVALID_DISPLAY_NAME = 'Please provide a valid display_name'
    INVALID_EMAIL = 'Please provide a valid email.'
    INVALID_PASSWORD = 'Please provide a valid password'
    INVALID_PASSWORD_LENGTH = 'password length must be between {min} and {max}.'
    INVALID_USER_ID = 'Please provide a valid user_id.'
    ATTR_REQUIRED = 'attr is required'
    USER_WITH_EMAIL_ID_ALREADY_EXISTS = 'User with this email id already exists.'
    USER_WITH_DISPLAY_NAME_ALREADY_EXISTS = 'User with this display_name already exists.'
    NO_USER_FOUND = 'User not registered'
    EMAIL_REQUIRED = 'email is required.'
    USER_ID_REQUIRED = 'user_id is required'
    DISPLAY_NAME_REQUIRED = 'display_name is required.'
    PASSWORD_REQUIRED = 'password is required.'
    INVALID_CREDENTIALS = 'Invalid email or password'
