"""This module holds all the configurations."""

from os import environ

from user_accounts.common.constants import Constants


class Config:
    DB_CONNECTION_STRING = environ.get(Constants.DB_CONNECTION_STRING)
    MINIMUM_HASH_ITERATION = environ.get(Constants.MINIMUM_HASH_ITERATION)
    MAXIMUM_HASH_ITERATION = environ.get(Constants.MAXIMUM_HASH_ITERATION)
