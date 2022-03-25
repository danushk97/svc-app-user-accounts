import pytest

from user_accounts.infrastructure._repository._abstract_repository import AbstractRepository


class Repository(AbstractRepository):
    def add(self, entity):
        super().add(entity)


def test_abstract_add_rasies_not_implemented_error(mocker):
    with pytest.raises(NotImplementedError):
        assert Repository().add("entity")
