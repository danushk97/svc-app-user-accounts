"""
This moudule acts as the service layer which helps to create, delete and update
user account detail.
"""

from injector import inject
from apputils.error_handler import ErrorHandler

from user_accounts.infrastructure.unit_of_work.postgres import \
    PostgresUnitOfWork
from user_accounts.common import exception
from user_accounts.domain.user import User
from user_accounts.application.validator.user_validator import UserValidator
from user_accounts.application.base_service import BaseService


class UserService(BaseService):
    """
    Holds business usecase/logic which are related to user
    creation/updation/deletion.

    Attributes:
        postgres_unit_of_work (PostgresUnitOfWork): Helps communicating with
        the postgres database.
        validator (UserValidator): Helps to validate user data.
    """
    @inject
    def __init__(self, unit_of_work: PostgresUnitOfWork,
                 validator: UserValidator):
        """
        Instantiates the class.
        """
        self.unit_of_work = unit_of_work
        self.validator = validator

    @ErrorHandler.handle_exception([exception.PostgresRepositoryException],
                                   exception.UserServiceException)
    def create_user(self, user_info: dict) -> dict:
        """
        Creates user.

        Args:
            user_info (dict): Basic user information.

        Returns:
            user_id: Generated id of the user.
        """
        user = self.__get_user_object(user_info)
        self.validator.validate_user(user)
        user_id = self.initiate_db_transaction(self.__create_user, user)

        return {
            'user_id': user_id
        }

    def __create_user(self, unit_of_work, user: User):
        repository = unit_of_work.user_repository()
        self.validator.validate_is_unique_user(user, repository)
        user_model = user.get_postgres_user_model()
        repository.add(user_model)
        unit_of_work.flush()
        password = user.password.get_postgres_password_model(
            user_model.stable_id
        )
        repository.add(password)
        unit_of_work.commit()

        return user_model.id

    def __get_user_object(self, props: dict) -> User:
        """
        Instantiates User object.

        Args:
            props (dict):

        Returns:
            User
        """
        return User(**props)
