"""
Holds the abstract class for unit of work.
"""

from abc import ABC, abstractmethod


class AbstractUnitOfWork(ABC):

    @abstractmethod
    def commit(self):
        raise NotImplementedError

    @abstractmethod
    def rollback(self):
        raise NotImplementedError

    @abstractmethod
    def end_session(self):
        raise NotImplementedError
