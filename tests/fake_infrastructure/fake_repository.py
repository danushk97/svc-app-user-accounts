import os
import bcrypt
from random import randint
from tests.fake_error_code.fake_error_code import FakeErrorCode

from user_accounts.common.exception import PostgresRepositoryException


class FakePostgresRepository:
    def __init__(self, session):
        self.session = session

    def add(self, entity):
        entity.id = 1
        return None


class FakeUserRepositoryReturnsEmptyList(FakePostgresRepository):
    def get_user_by_attr_field(self, field, value):
        return []


class FakeUserRepositoryRasisesRepoException(FakePostgresRepository):
    def get_user_by_attr_field(self, field, value):
        raise PostgresRepositoryException([FakeErrorCode.REPO_ERROR])


class FakePasswordRepositoryRasisesRepoException(FakePostgresRepository):
    def update_password_by_user_id(self, user_id, password):
        raise PostgresRepositoryException([FakeErrorCode.REPO_ERROR])

    def get_password_hash_by_email(self, user_id):
        raise PostgresRepositoryException([FakeErrorCode.REPO_ERROR])


class FakeUserRepository(FakePostgresRepository):
    def get_user_by_attr_field(self, field, value):
        return [{'user_id': 'user_id'}]


class FakePasswordRepository(FakePostgresRepository):
    def update_password_by_user_id(self, user_id, password):
        return 1

    def get_password_hash_by_email(self, user_id):
        minimum_hash_iteration = os.environ.get('MINIMUM_HASH_ITERATION')
        maximum_hash_iteration = os.environ.get('MAXIMUM_HASH_ITERATION')
        hashing_itertation = randint(int(minimum_hash_iteration),
                                     int(maximum_hash_iteration))
        salt = bcrypt.gensalt(rounds=hashing_itertation)
        return user_id, bcrypt.hashpw('password'.encode('utf-8'), salt).decode('utf-8')


class FakePasswordRepositoryReturnsZero(FakePostgresRepository):
    def update_password_by_user_id(self, user_id, password):
        return 0

    def get_password_hash_by_email(self, user_id):
        return None
