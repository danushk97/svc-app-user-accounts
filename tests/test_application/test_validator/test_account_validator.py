import pytest

from tests.helpers.fake_infrastructure.fake_repository import FakeAccountRepository

from useraccounts.application.validator.account_validator import AccountValidator
from useraccounts.application.validator.exception import DuplicateEntryException


def test_validate_for_create_account_given_valid_account_returns_none(account_schema_instance):
    result = AccountValidator.validate_for_create(account_schema_instance, FakeAccountRepository())
    assert result is None


def test_validate_for_create_account_given_existing_account_detail_raises_exception(account_schema_instance):
    account_schema_instance.username = 'existing_uname'
    account_schema_instance.email = 'existing_email'

    with pytest.raises(DuplicateEntryException) as error:
        AccountValidator.validate_for_create(account_schema_instance, FakeAccountRepository())

    assert error._excinfo[1].status == 400
    assert error._excinfo[1].invalid_params == [
        {
            'field': 'email',
            'message': 'Account with this email id already exists.'
        },
        {
            'field': 'username',
            'message': 'Account with this username already exists.'
        }
    ]
