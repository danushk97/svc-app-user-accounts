import pytest
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from testcontainers.postgres import PostgresContainer

from useraccounts.adapters.sqlalchemy.orm import start_orm_mappers
from useraccounts.domain.models import Account, Password


class ChildPostgresContainer(PostgresContainer):
    def get_connection_url(self, host=None):
        return super().get_connection_url().replace('localnpipe', 'localhost')


def init_test_data(engine):
    session = sessionmaker(engine)
    with session() as sess:
        with sess.begin():
            account = Account(
                'fake_name',
                '11-11-2023',
                'fake_uname',
                'uname@fakemail.com',
                1234567890
            )
            account.password = Password(b'password')
            sess.add(account)


@pytest.fixture(scope='session')
def db_session():
    postgres_container = ChildPostgresContainer()
    with postgres_container as container:
        os.environ['DB_CONNECTION_URL'] = container.get_connection_url()
        engine = create_engine(os.environ['DB_CONNECTION_URL'])
        start_orm_mappers(is_create_tables=True, engine=engine)
        init_test_data(engine)
        yield sessionmaker(engine)
