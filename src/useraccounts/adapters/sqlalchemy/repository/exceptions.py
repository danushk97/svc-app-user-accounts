from sqlalchemy.exc import SQLAlchemyError

from appscommon.exception import AppException


def sql_error_handler(src_fn):
    def wrapper(*args, **kwargs):
        try:
            return src_fn(*args, **kwargs)
        except SQLAlchemyError as sql_err:
            raise AppException() from sql_err

    return wrapper
