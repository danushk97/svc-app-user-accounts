"""
This module holds the class which defines password entity.
"""

import logging
import bcrypt

from useraccounts.domain.value_object._value_object import ValueObject
from useraccounts.infrastructure.sqlalchemy.models.password import PasswordModel


logger = logging.getLogger(__name__)


class Password(ValueObject):
    """
    Password is a value object.

    Attributes:
        password_str (str): password string.
        password_hash (str): encrypted form of password_str.
    """
    def __init__(self, password_hash: bytes, user_id=None):
        """
        Instantiates class.
        """

        self.user_id = user_id
        self.hash = password_hash

    def get_password_model(self):
        return PasswordModel(hash=self.hash)

    @staticmethod
    def do_match(password: bytes, hashed_password: bytes) -> bool:
        return bcrypt.checkpw(password, hashed_password)
