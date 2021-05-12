from tests.fake_infrastructure.fake_sqlalchmey_session import \
    FakeSQLAlchemySession
from user_accounts.infrastructure.unit_of_work.postgres import \
    PostgresUnitOfWork
from user_accounts.infrastructure.repository.user_repository import \
    UserRepository
from user_accounts.infrastructure.repository.password_repository import \
    PasswordRepository


potgres_unit_of_work = PostgresUnitOfWork(session_factory=FakeSQLAlchemySession)


def test_postgres_unit_of_work():
    with potgres_unit_of_work as postgres:
        assert postgres.commit() is None
        assert postgres.flush() is None
        assert isinstance(postgres.user_repository(), UserRepository)
        assert isinstance(postgres.password_repository(), PasswordRepository)
