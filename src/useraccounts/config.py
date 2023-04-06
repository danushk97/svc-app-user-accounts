"""
This module holds all the configurations.
"""

from dotenv import load_dotenv
from os import environ

from useraccounts.constants import Constants


required_configs = [
    Constants.DB_CONNECTION_STRING,
    Constants.MINIMUM_HASH_ITERATION,
    Constants.MAXIMUM_HASH_ITERATION
]


config = {
    c: ''
    for c in required_configs
}


def init_config() -> None:
    load_dotenv(f'{environ[Constants.FLASK_ENV]}.env')
    for key in config:
        config[key] = environ.get(key)
