from abc import ABC, abstractmethod

from useraccounts.domain.entity._entity import Entity


class AbstractRepository(ABC):

    @abstractmethod
    def add(self, entity: Entity):
        raise NotImplementedError
