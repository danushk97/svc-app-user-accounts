"""
This module holds the class which defines user entity.
"""

from typing import Any

from user_accounts.common.constants import Constants
from user_accounts.domain.password import Password
from user_accounts.domain.postgres_models.user import User as UserModel


class User:
    """
    User is an entity.

    Attributes:
        email (str): User's email id.
        display_name (str): User's profile name.
        phone_number (int): User's phone number.
        password (Password): User's password.
    """
    def __init__(self, password:Password=None, **kwargs):
        """
        Instantiates the class.
        """
        self.email = kwargs.get(Constants.EMAIL)
        self.display_name = kwargs.get(Constants.DISPLAY_NAME)
        self.phone_number = kwargs.get(Constants.PHONE_NUMBER)
        self.password = password

    @property
    def email(self):
        return self.__email

    @property
    def display_name(self):
        return self.__display_name

    @property
    def phone_number(self):
        return self.__phone_number

    @property
    def password(self):
        return self.__password

    @email.setter
    def email(self, email: str):
        self.__email = email

    @display_name.setter
    def display_name(self, display_name: str):
        self.__display_name = display_name

    @phone_number.setter
    def phone_number(self, phone_number: int):
        self.__phone_number = phone_number

    @password.setter
    def password(self, password: Password):
        if isinstance(password, Password):
            self.__password = password

    def is_valid(self) -> bool:
        """
        Checks whether all the props in this is object are valid.
        """
        user_props = self.__dict__
        password_key = '_User__password'

        if not password_key in user_props:
            return False

        for key, value in user_props.items():
            if not value:
                return False

            if key == '_User__phone_number' and not self.__is_valid_phone_number():
                return False

            if key == password_key and not self.password.is_valid():
                return False

        return True

    def __is_valid_phone_number(self) -> bool:
        """
        Validates whether the phone_number is instance of int and checks whether
        the length of the phone number is 10.
        """
        if not isinstance(self.phone_number, int) or len(str(self.phone_number)) != 10:
            return False

        return True

    def get_postgres_user_model(self):
        if self.is_valid():
            attr = {
                Constants.DISPLAY_NAME: self.display_name,
                Constants.EMAIL: self.email,
                Constants.PHONE_NUMBER: self.phone_number
            }
            return UserModel(attr=attr)
