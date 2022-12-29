"""
Holds the abstract class for unit of work.
"""

from abc import ABC, abstractmethod

from useraccounts.application.interfaces.accounts_repository import AbstractAccountsRepository


class AbstractUnitOfWork(ABC):
    accounts: AbstractAccountsRepository

    def __enter__(self):
        """
        Gets executed when this instance of class is used with "with" statement.
        """
        return self

    
    def __exit__(self, *args) -> None:
        """
        Gets executed after the code within the "with" statement gets executed.
        """
        pass

    @abstractmethod
    def flush(self):
        raise NotImplementedError

    @abstractmethod
    def commit(self):
        raise NotImplementedError

    @abstractmethod
    def rollback(self):
        raise NotImplementedError

    @abstractmethod
    def end_session(self):
        raise NotImplementedError
