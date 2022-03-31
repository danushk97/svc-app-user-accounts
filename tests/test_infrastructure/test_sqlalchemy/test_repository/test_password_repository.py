import pytest

from tests.helpers.fake_infrastructure.fake_sqlalchmey_session import FakeSQLAlchemySession, FakeUnitOfWorkRaisesSqlError

from user_accounts.infrastructure.sqlalchemy.repository.password_repository import PasswordRepository
from user_accounts.common.exception import RepositoryException


@pytest.fixture
def password_repo():
    return PasswordRepository(FakeSQLAlchemySession())


@pytest.fixture
def password_repo_raise_sql_error():
    return PasswordRepository(FakeUnitOfWorkRaisesSqlError())


def test_get_user_given_valid_data_returns_affected_row(password_repo):
    assert password_repo.update_password_by_user_id('key', 'value') == 1
    assert password_repo.update_password_by_user_id('key', 'invalid') == 0


def test_add_rasies_postgres_repo_exception_on_sql_error(password_repo_raise_sql_error):
    with pytest.raises(RepositoryException):
        password_repo_raise_sql_error.update_password_by_user_id('key', 'value')
