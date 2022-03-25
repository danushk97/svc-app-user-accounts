from tests.fake_infrastructure.fake_sqlalchmey_session import FakeSQLAlchemySession
from user_accounts.infrastructure.sqlalchemy.unit_of_work import SQLAlchemyUnitOfWork
from user_accounts.infrastructure.sqlalchemy.repository.user_repository import UserRepository
from user_accounts.infrastructure.sqlalchemy.repository.password_repository import PasswordRepository


potgres_unit_of_work = SQLAlchemyUnitOfWork(session_factory=FakeSQLAlchemySession)


def test_sqlalchemy_unit_of_work():
    with potgres_unit_of_work as sqlalchemy:
        assert sqlalchemy.commit() is None
        assert sqlalchemy.flush() is None
        assert isinstance(sqlalchemy.user_repository(), UserRepository)
        assert isinstance(sqlalchemy.password_repository(), PasswordRepository)
