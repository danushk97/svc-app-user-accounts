from datetime import datetime
from uuid import uuid4
from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.dialects import postgresql

from user_accounts.infrastructure.sqlalchemy.models import Base
from user_accounts.common.constants import Constants


class PasswordModel(Base):
    __tablename__ = 'user_password'

    id = Column(Integer, primary_key=True)
    stable_id = Column(postgresql.UUID, nullable=False)
    user_id = Column(postgresql.UUID, ForeignKey('user_accounts.stable_id'), nullable=False)
    attr = Column(postgresql.JSONB, nullable=False)
    active_flag = Column(postgresql.BOOLEAN, nullable=False, default=True)
    created_date = Column(DateTime, default=datetime.utcnow, nullable=False)

    def __init__(self, **kwargs):
        """
        Instantiates the class.
        """
        self.stable_id = kwargs.get(Constants.STABLE_ID, str(uuid4()))
        self.attr = kwargs.get(Constants.ATTR)
