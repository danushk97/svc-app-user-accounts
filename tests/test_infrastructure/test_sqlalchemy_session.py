import pytest
import os
from sqlalchemy.orm import Session

from user_accounts.infrastructure.sqlalchemy_session import SQLAlchemySessionFactory


def test_sqlalchemy_get_instance_on_calling_twice_should_return_same_instance(postgres_container):
    db_connection_url = os.environ.get('db_connection_url')
    session_1 = SQLAlchemySessionFactory.get_instance(db_connection_url)
    session_2 = SQLAlchemySessionFactory.get_instance(db_connection_url)

    assert isinstance(session_2(), Session)
    assert session_2.remove() is None
    assert session_1 == session_2

    #raises exception while trying instantiate via __init__, given it has
    #instantiated once already
    with pytest.raises(Exception):
        SQLAlchemySessionFactory(db_connection_url)