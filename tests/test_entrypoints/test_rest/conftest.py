import pytest

from tests.helpers.fake_config import fake_config
from tests.helpers.fake_infrastructure.fake_unit_of_work import FakeUnitOfWork

from useraccounts.app import flask_app
from useraccounts.bootstrap import bootstrap


# @pytest.fixture(autouse=True, scope='session')
# def test_init(monkeypatch):
#     monkeypatch.setenv('MINIMUM_HASH_ITERATION', '4')
#     monkeypatch.setenv('MAXIMUM_HASH_ITERATION', '12')
#     monkeypatch.setenv('DB_CONNECTION_STRING', 'fake_string')


@pytest.fixture(scope='session')
def test_client():
    bootstrap(unit_of_work=FakeUnitOfWork(), isstart_orm_mappers=False)
    with flask_app().test_client() as http_client:
        yield http_client


# @pytest.fixture
# def client_raises_exception():
#     with create_app(di_configurator=test_di_exception_config).test_client() as http_client:
#         yield http_client
