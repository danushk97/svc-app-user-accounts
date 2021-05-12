import pytest

from tests.fake_infrastructure.fake_sqlalchmey_session import \
    FakeSQLAlchemySession, FakeUnitOfWorkRaisesSqlError

from user_accounts.infrastructure.repository.postgres_repository import \
    PostgresRepository
from user_accounts.common.exception import PostgresRepositoryException


@pytest.fixture
def postgres_repo():
    return PostgresRepository(FakeSQLAlchemySession())


@pytest.fixture
def postgres_repo_raise_sql_error():
    return PostgresRepository(FakeUnitOfWorkRaisesSqlError())


def test_add_given_valid_data_returns_none(postgres_repo):
    assert postgres_repo.add('entity') is None


def test_add_rasies_postgres_repo_exception_on_sql_error(postgres_repo_raise_sql_error):
    with pytest.raises(PostgresRepositoryException):
        postgres_repo_raise_sql_error.add('entity')
