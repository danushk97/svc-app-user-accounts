from datetime import date, datetime

from appscommon.domain.models import BaseModel

from useraccounts.domain.models.password import Password
from useraccounts.schemas.account import CreateAccountRequestSchema


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
        is_active: bool = True,
        created_at: datetime = None,
        created_by: str = None,
        updated_by: str = None,
        updated_at: datetime = None
    ) -> None:
        super().__init__(
            created_by,
            created_at,
            updated_by,
            updated_at,
            is_active
        )
        self.id = None
        self.stable_id = None
        self.name = name
        self.dob = dob
        self.username = username
        self.email = email
        self.phone_number = phone_number
        self.isemail_verified = isemail_verified
        self.isphone_number_verfied = isphone_number_verfied
        self._password: Password = None

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value: Password):
        assert isinstance(value, Password), "value must be a instance of Password"
        self._password = value

    @classmethod
    def from_create_account_schema(cls, schema: CreateAccountRequestSchema):
        account = cls(
            schema.name,
            schema.dob,
            schema.username,
            schema.email,
            schema.phone_number
        )
        passowrd = Password(schema.password)
        account.password = passowrd

        return account
