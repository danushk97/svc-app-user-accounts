import pytest

from appscommon.exception import AppException
from sqlalchemy.exc import SQLAlchemyError

from useraccounts.adapters.sqlalchemy.repository.accounts_repository import AccountsRepository
from useraccounts.domain.models import Account


@pytest.fixture(scope="function")
def accounts_repo(db_session):
    with db_session() as sess:
        yield AccountsRepository(sess)


@pytest.mark.parametrize(
    "input_uname, expected_instance", [
        ("fake_uname", Account),
        ("fake_non_exist", None)
    ]
)
def test_get_by_username_given_valid_username_then_returns_data_if_exists(accounts_repo, input_uname, expected_instance):
    account_row = accounts_repo.get_by_username(input_uname)
    if expected_instance:
        assert isinstance(account_row, expected_instance)
        assert account_row.username == input_uname
    else:
        assert account_row is None


@pytest.mark.parametrize(
    "input_email, expected_instance", [
        ("uname@fakemail.com", Account),
        ("fake_non_exist", None)
    ]
)
def test_get_by_username_given_valid_email_then_returns_data_if_exists(accounts_repo, input_email, expected_instance):
    account_row = accounts_repo.get_by_email(input_email)
    if expected_instance:
        assert isinstance(account_row, expected_instance)
        assert account_row.email == input_email
    else:
        assert account_row is None


def test_get_by_username_given_invalid_input_raises_app_exception(accounts_repo):
    with pytest.raises(AppException) as exc:
        accounts_repo.get_by_email(1)
    assert isinstance(exc._excinfo[1].__cause__, SQLAlchemyError)


def test_get(accounts_repo):
    with pytest.raises(NotImplementedError):
        accounts_repo.get(1)


def test_list(accounts_repo):
    with pytest.raises(NotImplementedError):
        accounts_repo.list()
