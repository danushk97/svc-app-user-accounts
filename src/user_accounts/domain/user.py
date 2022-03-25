"""
This module holds the class which defines user entity.
"""
import re

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
    def __init__(self, **kwargs):
        """
        Instantiates the class.
        """
        self.email = kwargs.get(Constants.EMAIL)
        self.display_name = kwargs.get(Constants.DISPLAY_NAME)
        self.password = Password(kwargs.get(Constants.PASSWORD, ''))

    @property
    def password(self) -> Password:
        return self.__password

    @password.setter
    def password(self, password: Password) -> None:
        if not isinstance(password, Password):
            raise ValueError('password must be instance of password')

        self.__password = password

    def isvalid_display_name(self) -> bool:
        return bool(self.display_name)

    def isvalid_email(self) -> bool:
        return re.search('^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$',
                         self.email) is not None

    def isvalid_password(self) -> bool:
        return self.password.is_valid()

    def is_valid(self) -> bool:
        """
        Checks whether all the props in this is object are valid.
        """
        return self.isvalid_display_name() and self.isvalid_email() and \
                self.isvalid_password()

    def get_postgres_user_model(self) -> UserModel:
        """
        Returns None if the user is not valid.
        """
        if self.is_valid():
            attr = {
                Constants.DISPLAY_NAME: self.display_name,
                Constants.EMAIL: self.email,
            }
            return UserModel(attr=attr)
