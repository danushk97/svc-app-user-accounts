import pytest

from user_accounts.infrastructure.repository.abstract_repository import \
    AbstractRepository


def test_abstract_add_rasies_not_implemented_error():
    with pytest.raises(NotImplementedError):
        assert AbstractRepository().add("entity")
