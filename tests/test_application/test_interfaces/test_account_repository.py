import pytest

from useraccounts.application.interfaces.accounts_repository import AbstractAccountsRepository


class AccountRepository(AbstractAccountsRepository):
    def get_by_email(self, email: str):
        return super().get_by_email(email)

    def get_by_username(self, username: str):
        return super().get_by_username(username)
    
    def get_by_phone_number(self, phone_number: int):
        return super().get_by_phone_number(phone_number)

    def list(self):
        return super().list()

    def get(self, id):
        return super().get(id)


def test_abstract_account_repository():
    account_repo = AccountRepository()
    with pytest.raises(NotImplementedError):
        account_repo.get_by_email('test@mail.com')

    with pytest.raises(NotImplementedError):
        account_repo.get_by_username('fake_uname')

    with pytest.raises(NotImplementedError):
        account_repo.get_by_phone_number(1234567890)