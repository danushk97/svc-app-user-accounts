"""
This module holds a class which defines auth error codes.
"""

from apputils.error_codes.error_codes import ErrorCodes


class AuthErrorCodes(ErrorCodes):
    """
    Holds the error codes related to invalid credential.
    """
    INVALID_CREDENTIALS = (6000, 'Invalid credentials')
