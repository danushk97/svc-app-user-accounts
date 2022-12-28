from useraccounts.application.interfaces.repository import AbstractRepository


class AbstractUsersRepository(AbstractRepository):
    def get_by_attr_field(self, field: str):
        raise NotImplementedError
        