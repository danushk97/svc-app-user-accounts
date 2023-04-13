from tests.helpers.fake_infrastructure.fake_unit_of_work import FakeUnitOfWork
from tests.helpers.fake_service.fake_account_validator import FakeAccountValidator

from useraccounts.application.service.accounts_service import AccountService


def test_create_account_given_valid_input_returns_none(account_schema_instance, monkeypatch):
    monkeypatch.setattr('useraccounts.application.service.accounts_service.AccountValidator', FakeAccountValidator)
    assert AccountService(FakeUnitOfWork()).create_account(account_schema_instance) is None
