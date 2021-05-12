from sqlalchemy.exc import SQLAlchemyError

class FakePassword:
    attr = {
        'credential': 'password_hash'
    }

class FakeSQLAlchemySession:
    def __init__(self, *args, **kwargs):
        """
        Pass
        """
        pass

    def __call__(self):
        return self

    @staticmethod
    def get_instance(db_connection_url):
        return FakeSQLAlchemySession()

    def join(self, *args):
        return self

    def add(self, entity):
        return None

    def update(self, value):
        if value['attr']['credential'] == 'invalid':
            return 0

        return 1

    def query(self, *args, **kwargs):
        return self

    def filter(self, *args, **kwargs):
        return self

    def all(self):
        return ['data']

    def one(self):
        return FakePassword

    def commit(self):
        return None

    def rollback(self):
        return None

    def flush(self):
        return None

    def remove(self):
        return None


class FakeUnitOfWorkRaisesSqlError:
    def add(self, entity):
        raise SQLAlchemyError

    def query(self, *args, **kwargs):
        raise SQLAlchemyError

    def update(self, value):
        raise SQLAlchemyError
