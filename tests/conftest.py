import pytest

from tests.fake_service.fake_user_service import FakeUserService, \
    FakeUserServiceRaisesException
from tests.fake_service.fake_password_service import FakePasswordService, \
    FakePasswordServiceRaisesException

from user_accounts import create_app
from user_accounts.application.user_service import UserService
from user_accounts.application.password_service import PasswordService


def test_di_config(binder):
    binder.bind(UserService, FakeUserService)
    binder.bind(PasswordService, FakePasswordService)


def test_di_exception_config(binder):
    binder.bind(PasswordService, FakePasswordServiceRaisesException)


@pytest.fixture
def client():
    with create_app(di_config=test_di_config).test_client() as http_client:
        yield http_client


@pytest.fixture
def client_raises_exception():
    with create_app(di_config=test_di_exception_config).test_client() as http_client:
        yield http_client


@pytest.fixture(autouse=True)
def test_init(monkeypatch):
    monkeypatch.setenv('minimum_hash_iteration', '4')
    monkeypatch.setenv('maximum_hash_iteration', '12')

