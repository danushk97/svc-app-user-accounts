import pytest
import jwt

from tests.fake_infrastructure.fake_unit_of_work import FakeUnitOfWork
from tests.fake_infrastructure.fake_unit_of_work import FakeEmptyUnitOfWorkRasiesRepoException
from tests.fake_infrastructure.fake_unit_of_work import FakeEmptyUnitOfWork
from user_accounts.application.password_service import PasswordService
from user_accounts.common.exception import InvalidPasswordException
from user_accounts.common.exception import InvalidRequestException
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


def test_update_password_given_invalid_user_id_raises_invalid_request_exception(password_service):
    with pytest.raises(InvalidRequestException) as excinfo:
        password_service.update_password('', 'password')
    assert excinfo.value.error_codes == [{'error_code': 4011, 'error_description': 'Please provide a valid user_id'}]

def test_update_password_given_invalid_password_raises_invalid_password_exception(password_service):
    with pytest.raises(InvalidPasswordException):
        password_service.update_password('user_id', 'invalid')


def test_update_password_given_valid_password_raises_password_service_exception_on_no_update(password_service_empty_repo):
    with pytest.raises(PasswordServiceException) as excinfo:
        password_service_empty_repo.update_password('is', 'password')
    assert excinfo.value.error_codes == [{'error_code': 4012, 'error_description': 'User not registered'} ]


def test_update_password_given_valid_password_raises_password_service_exception_on_repo_error(password_service_raises_exception):
    with pytest.raises(PasswordServiceException):
        password_service_raises_exception.update_password('user_id', 'password')


def test_update_password_given_valid_password_returns_none(password_service):
    assert password_service.update_password('user_id', 'password') is None


def test_update_password_given_invalid_user_id_raises_invalid_request_exception(password_service):
    with pytest.raises(InvalidRequestException) as excinfo:
        password_service.update_password('', 'password')
    assert excinfo.value.error_codes == [{'error_code': 4011, 'error_description': 'Please provide a valid user_id'}]


def test_validate_credential_given_invalid_email_raises_invalid_request_exception(password_service):
    with pytest.raises(InvalidRequestException) as excinfo:
        password_service.validate_credential('', 'password')
    assert excinfo.value.error_codes == [{'error_code': 4002, 'error_description': 'Please provide a valid email'}]


def test_validate_credential_given_invalid_password_raises_invalid_password_exception(password_service):
    with pytest.raises(InvalidCredetialException) as excinfo:
        password_service.validate_credential('user_id', 'invalid')
    assert excinfo.value.error_codes == [{'error_code': 6000, 'error_description': 'Invalid credentials'}]


def test_validate_credential_given_valid_password_raises_password_service_exception_on_no_update(password_service_empty_repo):
    with pytest.raises(PasswordServiceException):
        password_service_empty_repo.validate_credential('user_id', 'invalid_password')


def test_validate_credential_given_valid_password_raises_password_service_exception_on_repo_error(password_service_raises_exception):
    with pytest.raises(PasswordServiceException) as excinfo:
        password_service_raises_exception.validate_credential('user_id', 'password')
    assert excinfo.value.error_codes == [{'error_code': 0, 'error_description': 'repo error'}]


def test_validate_credential_given_valid_password_returns_jwt(password_service):
    jwt_token = password_service.validate_credential('user_id', 'password')
    assert jwt.decode(jwt_token, 'secret', algorithms=['HS256']) == {'user_id': 'user_id'}
