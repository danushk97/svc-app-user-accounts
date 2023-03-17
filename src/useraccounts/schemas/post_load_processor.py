import bcrypt
from random import randint
from os import environ

from useraccounts.config import config
from useraccounts.constants import Constants


def hash_password(password):
    hashing_itertation = randint(
        int(config.get(Constants.MINIMUM_HASH_ITERATION)),
        int(config.get(Constants.MAXIMUM_HASH_ITERATION))
    )
    return bcrypt.hashpw(
        password.encode('utf-8'),
        bcrypt.gensalt(rounds=hashing_itertation)
    )
