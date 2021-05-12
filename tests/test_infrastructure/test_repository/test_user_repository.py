import pytest

from tests.fake_infrastructure.fake_sqlalchmey_session import \
    FakeSQLAlchemySession, FakeUnitOfWorkRaisesSqlError

from user_accounts.infrastructure.repository.user_repository import \
    UserRepository
from user_accounts.common.exception import PostgresRepositoryException


@pytest.fixture
def user_repo():
    return UserRepository(FakeSQLAlchemySession())


@pytest.fixture
def user_repo_raise_sql_error():
    return UserRepository(FakeUnitOfWorkRaisesSqlError())


def test_get_user_given_valid_data_returns_list(user_repo):
    assert user_repo.get_user_by_attr_field('key', 'value') == ['data']


def test_add_rasies_postgres_repo_exception_on_sql_error(user_repo_raise_sql_error):
    with pytest.raises(PostgresRepositoryException):
        user_repo_raise_sql_error.get_user_by_attr_field('key', 'value')
