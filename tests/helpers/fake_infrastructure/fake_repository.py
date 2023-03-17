import os
import bcrypt
from random import randint

from tests.helpers.fake_error_code.fake_error_code import FakeErrorCode
from tests.helpers.fake_infrastructure.fake_sqlalchmey_session import FakeSQLAlchemySession



class FakeSQLAlchemyRepository:
    def __init__(self, session=FakeSQLAlchemySession()):
        self.session = session

    def add(self, entity):
        entity.stable_id = 1

        return entity


class FakeAccountRepository(FakeSQLAlchemyRepository):
    def add(self, account):
        return None

    def get_by_email(self, mail):
        if 'existing' in mail:
            return mail

        return None

    def get_by_username(self, username):
        if 'existing' in username:
            return username

        return None


class FakeUserRepositoryReturnsEmptyList(FakeSQLAlchemyRepository):
    def get_user_by_attr_field(self, field, value):
        return []


class FakeUserRepositoryRasisesRepoException(FakeSQLAlchemyRepository):
    def get_user_by_attr_field(self, field, value):
        raise RepositoryException([FakeErrorCode.REPO_ERROR])


class FakePasswordRepositoryRasisesRepoException(FakeSQLAlchemyRepository):
    def update_password_by_user_id(self, user_id, password):
        raise RepositoryException([FakeErrorCode.REPO_ERROR])


class FakeUserRepository(FakeSQLAlchemyRepository):
    def get_all_user_by_attr_field(self, field, value):
        return [{'user_id': 'user_id'}]

    def get_user_by_attr_field(self, field, value):
        minimum_hash_iteration = os.environ.get('MINIMUM_HASH_ITERATION')
        maximum_hash_iteration = os.environ.get('MAXIMUM_HASH_ITERATION')
        hashing_itertation = randint(int(minimum_hash_iteration), int(maximum_hash_iteration))
        salt = bcrypt.gensalt(rounds=hashing_itertation)

        return User(
            stable_id='test_user_id',
            attr={},
            password=Password(bcrypt.hashpw('password'.encode('utf-8'), salt))
        )


class FakePasswordRepository(FakeSQLAlchemyRepository):
    def update_password_by_user_id(self, user_id, password):
        return 1


class FakePasswordRepositoryReturnsZero(FakeSQLAlchemyRepository):
    def update_password_by_user_id(self, user_id, password):
        return 0
