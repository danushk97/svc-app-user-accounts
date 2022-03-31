import bcrypt
from random import randint

from user_accounts.config import Config


def hash_password(password):
    hashing_itertation = randint(
        int(Config.MINIMUM_HASH_ITERATION), int(Config.MAXIMUM_HASH_ITERATION)
    )
    return bcrypt.hashpw(
        password.encode('utf-8'),
        bcrypt.gensalt(rounds=hashing_itertation)
    )