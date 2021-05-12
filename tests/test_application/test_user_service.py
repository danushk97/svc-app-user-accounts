import pytest

from tests.fake_infrastructure.fake_unit_of_work import FakeUnitOfWork
from tests.fake_infrastructure.fake_unit_of_work import FakeEmptyUnitOfWork
from tests.fake_infrastructure.fake_unit_of_work import FakeEmptyUnitOfWorkRasiesRepoException

from user_accounts.application.user_service import UserService
from user_accounts.application.validator.user_validator import \
    UserValidator
from user_accounts.common.error_codes.invalid_user_error_codes import \
    InvalidUserErrorCodes
from user_accounts.common.exception import InvalidUserException
from user_accounts.common.exception import UserServiceException
from user_accounts.application.error_code_generator\
    .invalid_user_error_code_generator import InvalidUserErrorCodeGenerator


INVALID_EMAIL = {'error_code': 4002, 'error_description': 'Please provide a valid email'}
INVALID_PASSWORD= {'error_code': 4006, 'error_description': 'Please provide a valid password'}
INVALID_PHONE_NUMBER= {'error_code': 4003, 'error_description': 'Please provide a valid phone_number'}
INVALID_DISPLAY_NAME = {'error_code': 4001, 'error_description': 'Please provide a valid display_name'}
INVALID_PHONE_NUMBER_LENGTH = {'error_code': 4004, 'error_description': 'phone_number must be a 10 digit number'}
INVALID_PASSWORD_LENGTH = {'error_code': 4007, 'error_description': 'password length must be between 8 and 40'}
DUPLICATE_USER_DATA_ERROR_CODE = [{'error_code': 4008, 'error_description': 'User with this email id aleady exists'},
                       {'error_code': 4009, 'error_description': 'User with this display_name aleady exists'},
                       {'error_code': 4010, 'error_description': 'User with this phone_number aleady exists'}]
ERROR_CODE_GENERATOR = InvalidUserErrorCodeGenerator


@pytest.fixture
def user_service():
    return UserService(FakeUnitOfWork(), UserValidator(ERROR_CODE_GENERATOR()))


@pytest.fixture
def user_service_with_empty_repo():
    return UserService(FakeEmptyUnitOfWork(), UserValidator(ERROR_CODE_GENERATOR()))


@pytest.fixture
def user_service_raises_repo_exception():
    return UserService(FakeEmptyUnitOfWorkRasiesRepoException(),
                       UserValidator(ERROR_CODE_GENERATOR()))


def test_create_user_given_invalid_user_data_raises_invalid_user_exception(user_service):
    expected_error_codes = \
        [INVALID_EMAIL, INVALID_PHONE_NUMBER, INVALID_DISPLAY_NAME, INVALID_PHONE_NUMBER_LENGTH]
    with pytest.raises(InvalidUserException) as excinfo:
        user_service.create_user({'password': 'password'})

    assert excinfo.value.error_codes == expected_error_codes


def test_create_user_given_invalid_password_raises_invalid_user_exception(user_service):
    with pytest.raises(InvalidUserException) as excinfo:
        user_service.create_user({'email': 'email', 'display_name': 'name', 'phone_number': 1234567890})

    assert excinfo.value.error_codes == [INVALID_PASSWORD]


def test_create_user_given_invalid_phone_and_password_length_raises_invalid_user_exception(user_service):
    with pytest.raises(InvalidUserException) as excinfo:
        user_service.create_user({'email': 'email', 'display_name': 'name',
                                  'phone_number': 123456789, 'password': '123'})

    assert excinfo.value.error_codes == [INVALID_PHONE_NUMBER_LENGTH, INVALID_PASSWORD_LENGTH]


def test_create_user_given_invalid_password_length_raises_invalid_user_exception(user_service):
    with pytest.raises(InvalidUserException) as excinfo:
        user_service.create_user({'email': 'email', 'display_name': 'name',
                                  'phone_number': 1234567890, 'password': '123'})

    assert excinfo.value.error_codes == [INVALID_PASSWORD_LENGTH]


def test_create_user_given_valid_input_then_returns_user_id(user_service_with_empty_repo):
    data = user_service_with_empty_repo.create_user({
        'email': 'email',
        'display_name': 'display_name',
        'phone_number': 1234567890,
        'password': 'password'
    })
    assert data['user_id'] == 1


def test_create_user_given_duplicate_input_then_raises_invalid_user_exception(user_service):
    with pytest.raises(InvalidUserException) as excinfo:
        user_service.create_user({
            'email': 'email',
            'display_name': 'display_name',
            'phone_number': 1234567890,
            'password': 'password'
        })
    assert excinfo.value.error_codes == DUPLICATE_USER_DATA_ERROR_CODE


def test_create_user_on_repository_exception_user_service_exception(user_service_raises_repo_exception):
    with pytest.raises(UserServiceException) as excinfo:
        user_service_raises_repo_exception.create_user({
            'email': 'email',
            'display_name': 'display_name',
            'phone_number': 1234567890,
            'password': 'password'
        })
    assert excinfo.value.error_codes == [{'error_code': 5000, 'error_description': 'Internal server error'}]
