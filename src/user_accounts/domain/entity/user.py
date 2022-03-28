"""
This module holds the class which defines user entity.
"""
import re

from user_accounts.common.constants import Constants
from user_accounts.domain.value_object.password import Password
from user_accounts.infrastructure.sqlalchemy.models.user import UserModel
from user_accounts.domain.entity._entity import Entity


class User(Entity):
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
        self.stable_id = kwargs.get(Constants.STABLE_ID)
        self.attr = kwargs.get(Constants.ATTR, {})
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
        return bool(self.attr.get(Constants.DISPLAY_NAME))

    def isvalid_email(self) -> bool:
        return re.search('^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$',
                         self.attr.get(Constants.EMAIL, '')) is not None

    def isvalid_password(self) -> bool:
        return self.password.is_valid()

    def is_valid(self) -> bool:
        """
        Checks whether all the props in this is object are valid.
        """
        return self.isvalid_display_name() and self.isvalid_email() and self.isvalid_password()

    def get_user_model(self) -> UserModel:
        """
        Returns None if the user is not valid.
        """
        if self.is_valid():
            user_model = UserModel(
                attr=self.attr,
            )
            user_model.password.append(self.password.get_password_model())

            return user_model
