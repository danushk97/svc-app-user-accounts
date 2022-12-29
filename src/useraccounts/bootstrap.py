import logging

from flask import Flask
from common import configurer

from useraccounts.application.interfaces.unit_of_work import AbstractUnitOfWork
from useraccounts.application.service import SERVICES
from useraccounts.adapters.sqlalchemy.orm import start_orm_mappers
from useraccounts.adapters.sqlalchemy.unit_of_work import SQLAlchemyUnitOfWork
from useraccounts.blueprints import BLUEPRINTS
from useraccounts.constants import Constants
from useraccounts.config import Config


_logger = logging.getLogger(__name__)
_services = None


def bootstrap(
    app: Flask = None,
    unit_of_work: AbstractUnitOfWork = SQLAlchemyUnitOfWork()
):
    global _services

    if _services:
        return _services

    _logger.info('Bootstrapping....')
    configurer.ensure_configs(Config)
    configurer.register_error_handlers(app)

    
    _logger.info('Injecting dependencies....')
    dependencies = {
        Constants.UNIT_OF_WORK: unit_of_work
    }
    _services = configurer.inject_dependencies(SERVICES, dependencies)
    
    _logger.info('Registering blueprints....')
    configurer.register_blueprints(app, BLUEPRINTS)
    start_orm_mappers()
    _logger.info('Bootstrapping was successful.')

    return _services
