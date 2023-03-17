import pytest

from useraccounts.domain.models import Password
from useraccounts.schemas.post_load_processor import hash_password, config


@pytest.fixture()
def hashed_password(monkeypatch):
    monkeypatch.setitem(config, 'MINIMUM_HASH_ITERATION', '4')
    monkeypatch.setitem(config, 'MAXIMUM_HASH_ITERATION', '12')
    return hash_password('test')


@pytest.mark.parametrize(
    'input, expected', [
        (b'test', True),
        (b'wrong_password', False)
    ]
)
def test_do_match_password_given_valid_input_returns_boolean(input, expected, hashed_password):
    assert Password.do_match(input, hashed_password) == expected
