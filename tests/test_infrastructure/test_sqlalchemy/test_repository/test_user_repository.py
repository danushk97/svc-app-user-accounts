import pytest
from user_accounts.domain.value_object.password import Password

from tests.helpers.fake_infrastructure.fake_sqlalchmey_session import FakeSQLAlchemySession, FakeUnitOfWorkRaisesSqlError

from user_accounts.infrastructure.sqlalchemy.repository.user_repository import UserRepository
from user_accounts.common.exception import RepositoryException
from user_accounts.domain.entity.user import User


@pytest.fixture
def user_repo():
    return UserRepository(FakeSQLAlchemySession())


@pytest.fixture
def user_repo_raise_sql_error():
    return UserRepository(FakeUnitOfWorkRaisesSqlError())


def test_get_user_given_valid_data_returns_list(user_repo):
    assert user_repo.get_all_user_by_attr_field('key', 'value') == ['data']


def test_add_rasies_postgres_repo_exception_on_sql_error(user_repo_raise_sql_error):
    with pytest.raises(RepositoryException):
        user_repo_raise_sql_error.get_all_user_by_attr_field('key', 'value')


def test_get_user_by_attr_given_valid_data_returns_password_hash(user_repo):
    user = user_repo.get_user_by_attr_field('key', 'value')
    assert user.stable_id == 'user_id'
    assert user.password.hash == b'password_hash'


def test_get_get_user_by_attr_rasies_postgres_repo_exception_on_sql_error(user_repo_raise_sql_error):
    with pytest.raises(RepositoryException):
        user_repo_raise_sql_error.get_user_by_attr_field('user_id', 'value')


def test_add_user_by_attr_given_valid_data_returns_password_hash(user_repo):
    user = user_repo.add(User(attr={}, password=Password(b'hash')))
    assert user.stable_id is not None


def test_add_get_user_by_attr_rasies_postgres_repo_exception_on_sql_error(user_repo_raise_sql_error):
    with pytest.raises(RepositoryException):
        user_repo_raise_sql_error.add(User(attr={}, password=Password(b'hash')))
