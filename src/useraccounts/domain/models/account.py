from datetime import date, datetime

from useraccounts.domain.models.password import Password
from useraccounts.domain.models.base_model import BaseModel


class Account(BaseModel):
    def __init__(
        self,
        name: str,
        dob: date,
        username: str,
        email: str,
        phone_number: int,
        isemail_verified: bool = False,
        isphone_number_verfied: bool = False,
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
        self.name = name
        self.dob = dob
        self.username = username
        self.email = email
        self.phone_number = phone_number
        self.isemail_verified = isemail_verified
        self.isphone_number_verfied = isphone_number_verfied
        self.active_flag = active_flag
        self._password: Password = None
    
    @property
    def password(self):
        return self._password
    
    @password.setter
    def set_password(self, value: Password):
        assert isinstance(value, Password), "value must be a instance of Password"
        self._password = value
