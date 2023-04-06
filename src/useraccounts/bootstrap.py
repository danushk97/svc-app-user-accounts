"""
This modules holds the bootstrap function.
"""

from logging import getLogger

from appscommon.flaskutils import confighelper
from appscommon.db.interfaces.unit_of_work import AbstractUnitOfWork

from useraccounts.application.service import SERVICES
from useraccounts.adapters.sqlalchemy.orm import start_orm_mappers
from useraccounts.adapters.sqlalchemy.unit_of_work import SQLAlchemyUnitOfWork
from useraccounts.constants import Constants
from useraccounts.config import required_configs, config, init_config


_logger = getLogger(__name__)
_services = None


def bootstrap(
    unit_of_work: AbstractUnitOfWork = None,
    isstart_orm_mappers: bool = True
):
    global _services
    if _services:
        return _services

    _logger.info('Bootstrapping....')
    init_config()
    confighelper.ensure_configs(config, required_configs)

    dependencies = {
        Constants.UNIT_OF_WORK: unit_of_work or SQLAlchemyUnitOfWork()
    }
    _services = confighelper.inject_dependencies(SERVICES, dependencies)

    if isstart_orm_mappers:
        start_orm_mappers()

    _logger.info('Bootstrapping was successful.')

    return _services
