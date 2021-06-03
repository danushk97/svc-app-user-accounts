"""
This module holds the class which defines password entity.
"""
import logging
import os
import bcrypt
from random import randint

from user_accounts.common.exception import InvalidCredetialException
from user_accounts.common.constants import Constants
from user_accounts.domain.postgres_models.password import Password as \
    PasswordModel


logger = logging.getLogger(__name__)


class Password:
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
        minimum_hash_iteration = os.environ.get(Constants.MINIMUM_HASH_ITERATION)
        maximum_hash_iteration = os.environ.get(Constants.MAXIMUM_HASH_ITERATION)
        hashing_itertation = randint(int(minimum_hash_iteration),
                                     int(maximum_hash_iteration))
        self.password_str = password
        self.salt = bcrypt.gensalt(rounds=hashing_itertation)
        self.password_hash = bcrypt.hashpw(password.encode('utf-8'), self.salt)

    @property
    def password_str(self) -> str:
        return self.__password_str

    @property
    def salt(self) -> str:
        return self.__salt

    @property
    def password_hash(self) -> str:
        return self.__password_hash

    @password_str.setter
    def password_str(self, password: str) -> None:
        if not isinstance(password, str):
            raise ValueError('password value must be string')

        self.__password_str = password

    @password_hash.setter
    def password_hash(self, password_hash: bytes) -> None:
        self.__password_hash = password_hash

    @salt.setter
    def salt(self, salt: bytes) -> None:
        self.__salt = salt

    def is_valid(self) -> bool:
        """
        Validates whether the self.password_str is instance of str and
        length of self.password_str is between 8 and 40.
        """
        return isinstance(self.password_str, str) and 7 < len(self.password_str) < 41

    def get_postgres_password_model(self, user_id: str):
        password_attr = {
                            Constants.USER_ID: user_id,
                            Constants.ATTR: {
                                Constants.CREDENTIAL: \
                                self.password_hash.decode('utf-8')
                            }
                        }
        return PasswordModel(**password_attr)

    @staticmethod
    def validate_password(password: bytes, hashed_password: bytes) -> None:
        if not bcrypt.checkpw(password, hashed_password):
            raise InvalidCredetialException()