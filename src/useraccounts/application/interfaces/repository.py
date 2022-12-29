from abc import ABC, abstractmethod

from sqlalchemy.orm import Session

from useraccounts.domain.models.base_model import BaseModel

class AbstractRepository(ABC):
    _session: Session 
    
    def add(self, entity: BaseModel):
        self._session.add(entity)
    
    @abstractmethod
    def get(self, id):
        raise NotImplementedError
    
    @abstractmethod
    def list(self):
        raise NotImplementedError
        