"""
This module holds the class which defines user entity.
"""
from user_accounts.common.constants import Constants
from user_accounts.domain.password import Password
from user_accounts.domain.postgres_models.user import User as UserModel


class User:
    """
    User is an entity.

    Attributes:
        email (str): User's email id.
        display_name (str): User's profile name.
        password (Password): User's password.
    """
    def __init__(self, password:Password=None, **kwargs):
        """
        Instantiates the class.
        """
        self.email = kwargs.get(Constants.EMAIL)
        self.display_name = kwargs.get(Constants.DISPLAY_NAME)
        self.password = password

    @property
    def email(self):
        return self.__email

    @property
    def display_name(self):
        return self.__display_name

    @property
    def password(self):
        return self.__password

    @email.setter
    def email(self, email: str):
        self.__email = email

    @display_name.setter
    def display_name(self, display_name: str):
        self.__display_name = display_name

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

            if key == password_key and not self.password.is_valid():
                return False

        return True

    def get_postgres_user_model(self):
        if self.is_valid():
            attr = {
                Constants.DISPLAY_NAME: self.display_name,
                Constants.EMAIL: self.email,
            }
            return UserModel(attr=attr)
