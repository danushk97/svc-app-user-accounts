import pytest

from user_accounts.infrastructure._repository.user_repository import AbstractUserRepository


@pytest.fixture
def user_repo():
    class UserRepo(AbstractUserRepository):
        def add(self, entity):
            return super().add(entity)

        def get_user_by_attr_field(self, attr_field: str, attr_field_value: str) -> list:
            return super().get_user_by_attr_field(attr_field, attr_field_value)

        def get_all_user_by_attr_field(self, attr_field: str, attr_field_value: str) -> list:
            return super().get_all_user_by_attr_field(attr_field, attr_field_value)

    return UserRepo()


def test_get_user_by_attr_field_raises_not_implemented_error(user_repo: AbstractUserRepository):
    with pytest.raises(NotImplementedError):
        user_repo.get_user_by_attr_field('key', 'value')


def test_get_alluser_by_attr_field_raises_not_implemented_error(user_repo: AbstractUserRepository):
    with pytest.raises(NotImplementedError):
        user_repo.get_all_user_by_attr_field('key', 'value')
