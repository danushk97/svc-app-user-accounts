import logging
import inspect
from flask_injector import FlaskInjector
from os import abort

from user_accounts.config import Config
from user_accounts.initializer._blueprints import register_blueprints
from user_accounts.initializer._error_handlers import register_error_handlers
from user_accounts.initializer._dependency_injectors import di_configurator


logger = logging.getLogger(__name__)


def _ensure_configs():
    """
    Aborts application start up if there is any missing configuration.
    """
    missing_configs = []
    for key, value in inspect.getmembers(Config):
        if not key.startswith('_') and (value is None or str(value).strip() == ''):
            missing_configs.append(key)

    if missing_configs:
        logger.critical(f'Aborting application startup due to missing configs: {missing_configs}')
        abort(1)


def init_app(app, default_di_configurator=None):
    """
    Ensures Configs and initializes all required app extensions.
    """
    _ensure_configs()
    logger.info('Config validation was successful.')

    register_blueprints(app)
    register_error_handlers(app)

    #instansiating dependency injectors
    FlaskInjector(app, modules=[default_di_configurator or di_configurator])
