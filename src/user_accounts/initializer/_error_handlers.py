from apputils.error_handler import ErrorHandler

from user_accounts.common.exception import AppException


error_handler = ErrorHandler()


def register_error_handlers(app) -> None:
    """
    Registers routes with the app instance.

    Args:
        app (Flask): Instance of app.
    """
    app.register_error_handler(AppException, error_handler.app_error_handler)
    app.register_error_handler(Exception, error_handler.generic_error_handler)
    app.register_error_handler(404, error_handler.page_not_found_handler)
    app.register_error_handler(405, error_handler.method_not_allowed_handler)
