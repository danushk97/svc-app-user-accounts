from sqlalchemy.exc import SQLAlchemyError


class FakeAccount:
    stable_id = 'user_id'


class FakeSQLAlchemySession:
    def __init__(self, *args, **kwargs):
        """
        Pass
        """

    def __call__(self):
        return self

    @staticmethod
    def get_instance(db_connection_url):
        return FakeSQLAlchemySession()

    def join(self, *args):
        return self

    def add(self, entity):
        return None

    def add_all(self, entity):
        return None

    def update(self, value):
        if value['hash'] == 'invalid':
            return 0

        return 1

    def query(self, *args, **kwargs):
        return self

    def where(self, *args, **kwargs):
        return self

    def filter(self, *args, **kwargs):
        return self

    def all(self):
        return ['data']

    def one_or_none(self):
        return FakeAccount

    def limit(self, limit):
        return self

    def commit(self):
        return None

    def rollback(self):
        return None

    def flush(self):
        return None

    def close(self):
        return None


class FakeUnitOfWorkRaisesSqlError:
    def add(self, entity):
        raise SQLAlchemyError

    def query(self, *args, **kwargs):
        raise SQLAlchemyError

    def update(self, value):
        raise SQLAlchemyError
