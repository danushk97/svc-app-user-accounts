import pytest
from flask import Flask

from useraccounts.app import flask_app


@pytest.fixture(autouse=True)
def fake_bootstrap(monkeypatch):
    monkeypatch.setattr('useraccounts.app.bootstrap', lambda: None)
    monkeypatch.setattr('useraccounts.app.register_blueprints', lambda *args, **kwargs: None)


def test_create_app_should_return_instance_of_flask_app():
    app = flask_app()
    assert isinstance(app, Flask)


# def test_create_app_should_abort_on_missing_config(monkeypatch):
#     def mock_abort(x):
#         raise Exception('Start up aborted!')

#     monkeypatch.setitem('useraccounts.bootstrap.abort', mock_abort)
#     monkeypatch.setitem('useraccounts.config.config', 'DB_CONNECTION_STRING', None)

#     with pytest.raises(Exception) as excinfo:
#         flask_app()

#     assert excinfo.value.args[0] == 'Start up aborted!'
