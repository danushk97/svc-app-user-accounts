from abc import abstractmethod

from user_accounts.infrastructure._repository._abstract_repository import AbstractRepository


class AbstractPasswordRepository(AbstractRepository):

    @abstractmethod
    def update_password_by_user_id(self, user_id: str, password_hash: str) -> int:
        raise NotImplementedError
