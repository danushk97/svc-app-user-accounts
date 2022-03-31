import imp
import pytest
from flask import Flask

from user_accounts.manage import create_app


def test_create_app_should_return_instance_of_flask_app():
    app = create_app()
    assert isinstance(app, Flask)


def test_create_app_should_abort_on_missing_config(monkeypatch):
    def mock_abort(x):
        raise Exception('Start up aborted!')

    monkeypatch.setattr('user_accounts.initializer.Config.DB_CONNECTION_STRING', None)
    monkeypatch.setattr('user_accounts.initializer.abort', mock_abort)

    with pytest.raises(Exception) as excinfo:
        create_app()

    assert excinfo.value.args[0] == 'Start up aborted!'
