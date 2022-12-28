from abc import ABC, abstractmethod
from useraccounts.domain.models.base_model import BaseModel

class AbstractRepository(ABC):
    @abstractmethod
    def add(self, entity: BaseModel):
        raise NotImplemented
    
    @staticmethod
    def get(self, id):
        raise NotImplemented
    
    @staticmethod
    def list(self):
        raise NotImplemented
        