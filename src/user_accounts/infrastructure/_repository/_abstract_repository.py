from abc import ABC, abstractmethod

class AbstractRepository(ABC):

    @abstractmethod
    def add(self, entity):
        raise NotImplementedError
