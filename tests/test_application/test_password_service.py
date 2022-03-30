import pytest
import jwt

from tests.helpers.fake_infrastructure.fake_unit_of_work import FakeUnitOfWork
from tests.helpers.fake_infrastructure.fake_unit_of_work import FakeEmptyUnitOfWorkRasiesRepoException
from tests.helpers.fake_infrastructure.fake_unit_of_work import FakeEmptyUnitOfWork
from user_accounts.application.password_service import PasswordService
from user_accounts.common.exception import InvalidCredetialException
from user_accounts.common.exception import PasswordServiceException


@pytest.fixture(autouse=True)
def test_init(monkeypatch):
    monkeypatch.setenv('MINIMUM_HASH_ITERATION', 4)
    monkeypatch.setenv('MAXIMUM_HASH_ITERATION', 12)


@pytest.fixture
def password_service():
    return PasswordService(FakeUnitOfWork())


@pytest.fixture
def password_service_empty_repo():
    return PasswordService(FakeEmptyUnitOfWork())


@pytest.fixture
def password_service_raises_exception():
    return PasswordService(FakeEmptyUnitOfWorkRasiesRepoException())


def test_update_password_given_valid_password_raises_password_service_exception_on_no_update(password_service_empty_repo):
    with pytest.raises(PasswordServiceException) as excinfo:
        password_service_empty_repo.update_password('is', 'password')
    assert excinfo.value.error_codes == ['User not registered']


def test_update_password_given_valid_password_raises_password_service_exception_on_repo_error(password_service_raises_exception):
    with pytest.raises(PasswordServiceException):
        password_service_raises_exception.update_password('user_id', 'password')


def test_update_password_given_valid_password_returns_none(password_service):
    assert password_service.update_password('user_id', 'password') is None


def test_validate_credential_given_valid_password_returns_jwt(password_service):
    jwt_token = password_service.validate_credential({'email': 'test@t.com', 'password': 'password'})
    assert jwt.decode(jwt_token, 'secret', algorithms=['HS256']) == {'user_id': 'test_user_id'}


def test_validate_credential_given_invalid_password_raises_invalid_password_exception(password_service):
    with pytest.raises(InvalidCredetialException) as excinfo:
        password_service.validate_credential({'email': 'test@t.com', 'password': 'invalid'})
    assert excinfo.value.error_codes == ['Invalid email or password']


def test_validate_credential_given_valid_password_raises_password_service_exception_on_no_update(password_service_empty_repo):
    with pytest.raises(PasswordServiceException):
        password_service_empty_repo.validate_credential({'email': 'test@t.com', 'password': 'invalid_password'})
