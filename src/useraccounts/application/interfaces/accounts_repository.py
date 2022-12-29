from abc import abstractmethod

from useraccounts.application.interfaces.repository import AbstractRepository


class AbstractAccountsRepository(AbstractRepository):
    @abstractmethod
    def get_by_username(self, username: str):
        raise NotImplementedError
    
    @abstractmethod
    def get_by_email(self, email: str):
        raise NotImplementedError
        