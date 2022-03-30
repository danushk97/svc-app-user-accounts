"""
This module holds the class which defines user entity.
"""

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

    def get_user_model(self) -> UserModel:
        """
        Returns None if the user is not valid.
        """
        user_model = UserModel(
            attr=self.attr,
        )
        user_model.password.append(self.password.get_password_model())

        return user_model
