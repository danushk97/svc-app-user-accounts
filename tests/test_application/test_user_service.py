import pytest

from tests.helpers.fake_infrastructure.fake_unit_of_work import FakeUnitOfWork
from tests.helpers.fake_infrastructure.fake_unit_of_work import FakeEmptyUnitOfWork
from tests.helpers.fake_infrastructure.fake_unit_of_work import FakeEmptyUnitOfWorkRasiesRepoException

from user_accounts.application.user_service import UserService
from user_accounts.application.validator.user_validator import UserValidator
from user_accounts.common.exception import UserServiceException, DuplicateEntryException
from user_accounts.application.error_code_generator\
    .invalid_user_error_code_generator import InvalidUserErrorCodeGenerator


INVALID_EMAIL = 'Please provide a valid email.'
INVALID_PASSWORD= 'Please provide a valid password'
INVALID_DISPLAY_NAME = 'Please provide a valid display_name'
INVALID_PASSWORD_LENGTH = 'password length must be between 8 and 40.'
DUPLICATE_USER_DATA_ERROR_CODE = [
    'User with this email id already exists.',
    'User with this display_name already exists.'
]
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


def test_create_user_given_valid_input_then_returns_user_id(user_service_with_empty_repo):
    data = user_service_with_empty_repo.create_user({
        'attr':{
            'email': 'email@gmail.com',
            'display_name': 'name',
        },
        'password': 'password'
        }
    )
    assert data['user_id'] == 1


def test_create_user_given_duplicate_input_then_raises_invalid_user_exception(user_service):
    with pytest.raises(DuplicateEntryException) as excinfo:
        user_service.create_user({
        'attr':{
            'email': 'email@gmail.com',
            'display_name': 'display_name',
        },
        'password': 'password'
        }
    )
    assert excinfo.value.message == 'The data provided is not unique.'
    assert excinfo.value.errors == [
        {
            'field': 'email',
            'message': 'User with this email id already exists.'
        },
        {
            'field': 'display_name',
            'message': 'User with this display_name already exists.'
        },
    ]


def test_create_user_on_repository_exception_user_service_exception(user_service_raises_repo_exception):
    with pytest.raises(UserServiceException) as excinfo:
        user_service_raises_repo_exception.create_user({
        'attr':{
            'email': 'email@gmail.com',
            'display_name': 'display_name',
        },
        'password': 'password'
        })
    assert excinfo.value.message == ['repo error']
