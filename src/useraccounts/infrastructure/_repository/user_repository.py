from abc import abstractmethod

from useraccounts.infrastructure._repository._abstract_repository import AbstractRepository
from useraccounts.domain.entity._entity import Entity


class AbstractUserRepository(AbstractRepository):

    @abstractmethod
    def get_all_user_by_attr_field(self, attr_field: str, attr_field_value: str) -> list:
        raise NotImplementedError

    @abstractmethod
    def get_user_by_attr_field(self, attr_field: str, attr_field_value: str) -> Entity:
        raise NotImplementedError
