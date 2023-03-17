from tests.helpers.fake_infrastructure.fake_repository import FakeUserRepository, \
    FakeUserRepositoryReturnsEmptyList, FakeUserRepositoryRasisesRepoException,\
    FakePasswordRepository, FakePasswordRepositoryReturnsZero, \
    FakePasswordRepositoryRasisesRepoException, FakeAccountRepository
from tests.helpers.fake_infrastructure.fake_sqlalchmey_session import FakeSQLAlchemySession


class FakeUnitOfWork:
    def __init__(self, session=FakeSQLAlchemySession, db_url=None):
        self._session = session(db_url)
        self.accounts = FakeAccountRepository(self._session)

    def __enter__(self):
        return self

    def flush(self):
        return None

    def commit(self):
        return None

    def rollback(self):
        return None

    def end_session(self):
        return None

    def __exit__(self, *args):
        """
        Pass
        """
        pass


class FakeEmptyUnitOfWork(FakeUnitOfWork):
    def user_repository(self):
        return FakeUserRepositoryReturnsEmptyList(self.session)

    def password_repository(self):
        return FakePasswordRepositoryReturnsZero(self.session)


class FakeEmptyUnitOfWorkRasiesRepoException(FakeUnitOfWork):
    def user_repository(self):
        return FakeUserRepositoryRasisesRepoException(self.session)

    def password_repository(self):
        return FakePasswordRepositoryRasisesRepoException(self.session)
