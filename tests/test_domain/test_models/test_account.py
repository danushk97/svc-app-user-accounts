import pytest

from sqlalchemy.orm import clear_mappers
from useraccounts.domain.models import Account, Password


@pytest.fixture()
def account_instance():
    account = Account(
        'name',
        '2001-01-01',
        'fake_uname',
        'fake@fakemail.com',
        1234567890
    )
    yield account


def test_account_instance_given_valid_values_then_accepts(account_instance: Account):
    clear_mappers()
    account_instance.password = Password(b'test')
    assert account_instance.name == 'name'
    assert account_instance.username == 'fake_uname'
    assert account_instance.email == 'fake@fakemail.com'
    assert account_instance.phone_number == 1234567890
    assert account_instance.password.hash == b'test'


def test_account_instance_given_invalid_password_then_raises_assertion_error(account_instance: Account):
    with pytest.raises(AssertionError) as err:
        account_instance.password = b'test'

    assert err._excinfo[1].args[0] == 'value must be a instance of Password'
