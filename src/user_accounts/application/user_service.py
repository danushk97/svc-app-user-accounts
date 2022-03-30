"""
This moudule acts as the service layer which helps to create, delete and update
user account detail.
"""

from injector import inject
from apputils.error_handler import ErrorHandler

from user_accounts.infrastructure.sqlalchemy.unit_of_work import SQLAlchemyUnitOfWork
from user_accounts.common import exception
from user_accounts.domain.entity.user import User
from user_accounts.application.validator.user_validator import UserValidator
from user_accounts.application._service import Service


class UserService(Service):
    """
    Holds business usecase/logic which are related to user
    creation/updation/deletion.

    Attributes:
        unit_of_work (SQLAlchemyUnitOfWork): Helps communicating with
        the postgres database.
        validator (UserValidator): Helps to validate user data.
    """
    @inject
    def __init__(self, unit_of_work: SQLAlchemyUnitOfWork, validator: UserValidator):
        """
        Instantiates the class.
        """
        self.unit_of_work = unit_of_work
        self.validator = validator

    @ErrorHandler.handle_exception([exception.RepositoryException], exception.UserServiceException)
    def create_user(self, user_info: dict) -> dict:
        """
        Creates user.

        Args:
            user_info (dict): Basic user information.

        Returns:
            user_id: Generated id of the user.
        """
        user = self._get_user_object(user_info)
        user_id = self.initiate_db_transaction(self._create_user, user)

        return {
            'user_id': user_id
        }

    def _create_user(self, unit_of_work: SQLAlchemyUnitOfWork, user: User):
        repository = unit_of_work.user_repository()
        self.validator.validate_is_unique_user(user, repository)
        repository.add(user)
        unit_of_work.commit()

        return user.stable_id

    def _get_user_object(self, props: dict) -> User:
        """
        Instantiates User object.

        Args:
            props (dict):

        Returns:
            User
        """
        return User(**props)
