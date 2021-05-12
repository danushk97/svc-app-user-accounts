from abc import ABC

class AbstractRepository(ABC):
    def add(self, entity):
        raise NotImplementedError
