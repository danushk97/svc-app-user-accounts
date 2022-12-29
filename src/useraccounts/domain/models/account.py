from uuid import uuid4
from datetime import datetime

from useraccounts.domain.models.password import Password
from useraccounts.domain.models.base_model import BaseModel


class Account(BaseModel):
    def __init__(
        self,
        email: str,
        username: str,
        attr: dict,
        stable_id: str = None,
        isemail_verified: bool = False,
        active_flag: bool = True,
        created_at: datetime = None,
        created_by: str = None,
        updated_by: str = None,
        updated_at: datetime = None
    ) -> None:
        super().__init__(
            created_by,
            created_at,
            updated_by,
            updated_at
        )
        self.stable_id = stable_id or str(uuid4())
        self.username = username
        self.email = email
        self.attr = attr
        self.isemail_verified = isemail_verified
        self.active_flag = active_flag
        self._password: Password = None
    
    @property
    def password(self):
        return self._password
    
    @password.setter
    def set_password(self, value: Password):
        assert isinstance(value, Password), "value must be a instance of Password"
        self._password = value
