from logging import getLogger

from appscommon import configurer
from flask import Flask

from useraccounts.application.interfaces.unit_of_work import AbstractUnitOfWork
from useraccounts.application.service import SERVICES
from useraccounts.adapters.sqlalchemy.orm import start_orm_mappers
from useraccounts.adapters.sqlalchemy.unit_of_work import SQLAlchemyUnitOfWork
from useraccounts.constants import Constants
from useraccounts.config import Config
from useraccounts.entrypoints.rest import ROUTE_MODULES


_logger = getLogger(__name__)
_services = None


def bootstrap(
    flask_app: Flask = None,
    unit_of_work: AbstractUnitOfWork = SQLAlchemyUnitOfWork()
):
    global _services

    if _services:
        return _services

    _logger.info('Bootstrapping....')
    configurer.ensure_configs(Config)
    
    dependencies = {
        Constants.UNIT_OF_WORK: unit_of_work
    }
    _services = configurer.inject_dependencies(SERVICES, dependencies)
    
    if flask_app:
        configurer.register_http_error_handlers(flask_app)
        configurer.register_blueprints(flask_app, ROUTE_MODULES)
    
    start_orm_mappers()
    _logger.info('Bootstrapping was successful.')

    return _services
