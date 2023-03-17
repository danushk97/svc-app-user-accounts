from useraccounts.domain.models import Account, Password

def test_account_values():
    account = Account(
        'name',
        '2001-01-01',
        'fake_uname',
        'fake@fakemail.com',
        1234567890
    )
    account.password = Password(b'test')
    assert account.name == 'name'
    assert account.username == 'fake_uname'
    assert account.email == 'fake@fakemail.com'
    assert account.phone_number == 1234567890
    assert account.password.hash == b'test'