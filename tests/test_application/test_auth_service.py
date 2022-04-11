import pytest
import jwt

from tests.helpers.fake_infrastructure.fake_unit_of_work import FakeEmptyUnitOfWork, FakeUnitOfWork

from user_accounts.application.auth_service import AuthService
from user_accounts.common.exception import InvalidCredetialException, NoUserFoundException


@pytest.fixture(autouse=True)
def test_init(monkeypatch):
    monkeypatch.setenv('MINIMUM_HASH_ITERATION', 4)
    monkeypatch.setenv('MAXIMUM_HASH_ITERATION', 12)


@pytest.fixture
def auth_service():
    return AuthService(FakeUnitOfWork())


@pytest.fixture
def auth_service_empty_repo():
    return AuthService(FakeEmptyUnitOfWork())


def test_login_given_valid_login_data_returns_jwt(auth_service: AuthService):
    jwt_token = auth_service.login({'email': 'test@t.com', 'password': 'password'})
    assert jwt.decode(jwt_token, 'secret', algorithms=['HS256']) == {'user_id': 'test_user_id'}


def test_login_given_invalid_auth_raises_invalid_auth_exception(auth_service: AuthService):
    with pytest.raises(InvalidCredetialException) as excinfo:
        auth_service.login({'email': 'test@t.com', 'password': 'invalid'})
    assert excinfo.value.message == 'Invalid email or password'


def test_login_given_valid_auth_raises_auth_service_exception_on_no_update(
        auth_service_empty_repo: AuthService):
    with pytest.raises(NoUserFoundException):
        auth_service_empty_repo.login({'email': 'test@t.com', 'password': 'invalid_password'})
