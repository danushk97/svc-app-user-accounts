import logging
from uuid import uuid4

from sqlalchemy import (
    Column,
    DateTime,
    func,
    ForeignKey,
    Integer,
    JSON,
    Table
)
from sqlalchemy.dialects.postgresql import UUID, BYTEA, BOOLEAN, VARCHAR
from sqlalchemy.orm import registry, relationship

from useraccounts.domain import models


logger = logging.getLogger(__name__)
mapper_registry = registry()
default_columns = [
    Column("active_flag", BOOLEAN, nullable=False, server_default='true'),
    Column("created_by", UUID, nullable=False),
    Column("created_at", DateTime, nullable=False),
    Column("updated_by", UUID, nullable=False),
    Column("updated_at", DateTime, nullable=False, server_default=func.now())
] 


accounts = Table(
    "accounts",
    mapper_registry.metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("stable_id", UUID, nullable=False, unique=True, server_default=str(uuid4())),
    Column("username", VARCHAR(50), nullable=False, unique=True),
    Column("email", VARCHAR(128), nullable=False, unique=True),
    Column("attr", JSON, nullable=False),
    Column("isemail_verified", BOOLEAN, nullable=False, server_default='false'),
    Column("isphone_number_verified", BOOLEAN, nullable=False, server_default='false'),
    Column("active_flag", BOOLEAN, nullable=False, server_default='false'),
    Column("created_by", UUID),
    Column("created_at", DateTime, nullable=False, server_default=func.now()),
    Column("updated_by", UUID, nullable=False),
    Column("updated_at", DateTime, server_default=func.now())
)


passwords = Table(
    "passwords",
    mapper_registry.metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("username", ForeignKey("accounts.username")),
    Column("hash", BYTEA, nullable=False),
    Column("created_by", ForeignKey("accounts.stable_id")),
    Column("created_at", DateTime, nullable=False, server_default=func.now()),
    Column("updated_by", ForeignKey("accounts.stable_id"), ),
    Column("updated_at", DateTime, server_default=func.now())
)


def start_orm_mappers():
    logger.info("Starting orm mappers...")
    mapper_registry.map_imperatively(
        models.Account,
        accounts,
        properties={
            "password": relationship(
                models.Password, 
                foreign_keys=[passwords.c.username], 
                uselist=False
            )
        }
    )
    mapper_registry.map_imperatively(
        models.Password,
        passwords,
        properties={
            "created_by_user": relationship(
                models.Account, 
                foreign_keys=[passwords.c.created_by],
                viewonly=True
            ),
            "updated_by_user": relationship(
                models.Account, 
                foreign_keys=[passwords.c.updated_by],
                viewonly=True
            )
        }
    )
    logger.info("Successfully mapped orm's.")
