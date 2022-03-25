"""
Holds the abstract class for unit of work.
"""

from abc import ABC


class AbstractUnitOfWork(ABC):
    def commit(self):
        raise NotImplementedError

    def rollback(self):
        raise NotImplementedError

    def end_session(self):
        raise NotImplementedError
