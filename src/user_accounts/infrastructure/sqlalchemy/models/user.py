from datetime import datetime
from uuid import uuid4
from sqlalchemy import Column, Integer, DateTime
from sqlalchemy.dialects import postgresql

from user_accounts.infrastructure.sqlalchemy.models import Base
from user_accounts.common.constants import Constants


class UserModel(Base):
    __tablename__ = 'user_accounts'

    id = Column(Integer, primary_key=True)
    stable_id = Column(postgresql.UUID, nullable=False)
    attr = Column(postgresql.JSONB, nullable=False)
    created_date = Column(DateTime, default=datetime.utcnow, nullable=False)

    def __init__(self, **kwargs):
        """
        Instantiates the class.
        """
        self.stable_id = kwargs.get(Constants.STABLE_ID, str(uuid4()))
        self.attr = kwargs.get(Constants.ATTR)