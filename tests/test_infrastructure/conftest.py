import pytest
import os

from testcontainers.postgres import PostgresContainer


class ChildPostgresContainer(PostgresContainer):
    def get_connection_url(self):
        return super().get_connection_url().replace('localnpipe', 'localhost')


@pytest.fixture(scope='session')
def postgres_container():
    postgres_container = ChildPostgresContainer()
    with postgres_container as container:
        os.environ['db_connection_url'] = container.get_connection_url()
        yield
        os.environ.pop('db_connection_url')
