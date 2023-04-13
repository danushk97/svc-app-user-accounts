import pytest
from dataclasses import dataclass
from os import environ
from typing import Optional


environ['FLASK_ENV'] = 'test'


@dataclass
class CreateAccountSchema:
    name: str
    dob: str
    username: str
    phone_number: int
    email: str
    password: Optional[str] = None


@pytest.fixture()
def account_schema_instance():
    return CreateAccountSchema(
        name='fake_name',
        dob='2001-01-12',
        username='fake_uname',
        email='uname@fakemail.com',
        phone_number=1234567890
    )
