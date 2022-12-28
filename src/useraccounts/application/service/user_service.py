"""
This moudule acts as the service layer which helps to create, delete and update user account detail.
"""

from datetime import datetime
from uuid import uuid4

from useraccounts.application.validator.user_validator import UserValidator
from useraccounts.application.interfaces.unit_of_work import AbstractUnitOfWork
from useraccounts.domain.models import User, Password
from useraccounts.schemas.user import UserIdSchema
from useraccounts.constants import Constants


class UserService:
    """
    Holds business usecase/logic which are related to user creation/updation/deletion.

    Attributes:
        unit_of_work (AbstractUnitOfWork): Helps communicating with the postgres database.
    """
    def __init__(self, unit_of_work: AbstractUnitOfWork):
        """
        Instantiates the class.
        """
        self.unit_of_work = unit_of_work

    def create_user(self, create_user_schema: dict) -> UserIdSchema:
        """
        Creates user.

        Args:
            user_info (dict): Basic user information.

        Returns:
            (UserIdSchema): Contains the generated stable_id of the user.
        """
        user = User(
            attr=create_user_schema[Constants.ATTR]
        )
        import pdb; pdb.set_trace()
        with self.unit_of_work as uow:
            UserValidator.validate_for_create(
                user, uow.users
            )
            uow.users.add(user)
            uow.commit()
            user_stable_id = user.stable_id

        return UserIdSchema(user_id=user_stable_id)
