from abc import abstractmethod

from user_accounts.infrastructure._repository._abstract_repository import AbstractRepository


class AbstractUserRepository(AbstractRepository):

    @abstractmethod
    def get_user_by_attr_field(self, attr_field: str, attr_field_value: str) -> list:
        raise NotImplementedError
