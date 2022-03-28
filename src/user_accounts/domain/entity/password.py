"""
This module holds the class which defines password entity.
"""
import logging
import bcrypt
from xml.dom.minidom import Entity
from random import randint

from user_accounts.config import Config
from user_accounts.infrastructure.sqlalchemy.models.password import PasswordModel
from user_accounts.common.constants import Constants


logger = logging.getLogger(__name__)


class Password(Entity):
    """
    Password is an entity.

    Attributes:
        password_str (str): password string
        password_hash (str): Hash of the user's password
        salt (str): Some random string
    """
    def __init__(self, password: str):
        """
        Instantiates class.
        """
        hashing_itertation = randint(
            int(Config.MINIMUM_HASH_ITERATION), int(Config.MAXIMUM_HASH_ITERATION)
        )
        self.password_str = password
        self.attr = {
            Constants.HASH: bcrypt.hashpw(
                password.encode('utf-8'),
                bcrypt.gensalt(rounds=hashing_itertation)
            ).decode()
        }

    @property
    def password_str(self) -> str:
        return self._password_str

    @password_str.setter
    def password_str(self, password: str) -> None:
        if not isinstance(password, str):
            raise ValueError('password value must be string')

        self._password_str = password

    def is_valid(self) -> bool:
        """
        Validates whether the self.password_str is instance of str and
        length of self.password_str is between 8 and 40.
        """
        return isinstance(self.password_str, str) and 7 < len(self.password_str) < 41

    def get_password_model(self):
        return PasswordModel(**self.attr)

    @staticmethod
    def do_match(password: bytes, hashed_password: bytes) -> bool:
        return bcrypt.checkpw(password, hashed_password)
