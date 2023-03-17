from sqlalchemy.orm import scoped_session

from tests.helpers.fake_infrastructure.fake_sqlalchmey_session import FakeSQLAlchemySession

from useraccounts.adapters.sqlalchemy.unit_of_work import SQLAlchemyUnitOfWork
from useraccounts.adapters.sqlalchemy.repository import AccountsRepository


unit_of_work = SQLAlchemyUnitOfWork(session_factory=FakeSQLAlchemySession)


def test_sqlalchemy_unit_of_work():
    with unit_of_work as sqlalchemy:
        assert sqlalchemy.commit() is None
        assert sqlalchemy.flush() is None
        assert isinstance(sqlalchemy.accounts, AccountsRepository)


def test_sqlalchemy_unit_of_work_given_no_sessionmaker_then_should_create_one(monkeypatch):
    monkeypatch.setattr('useraccounts.adapters.sqlalchemy.unit_of_work.create_engine', lambda *args: None)
    monkeypatch.setattr('useraccounts.adapters.sqlalchemy.unit_of_work.scoped_session', lambda *args: 'scoped_session')
    monkeypatch.setattr('useraccounts.adapters.sqlalchemy.unit_of_work.sessionmaker', lambda bind=None: None)
    session_maker = SQLAlchemyUnitOfWork()._get_session_maker()
    assert session_maker == 'scoped_session'
