"""
This module holds request/response schemas for user related endpoints.
"""

from typing import Optional
from pydantic import BaseModel, EmailStr, validator, Field, PastDate

from useraccounts.schemas.post_load_processor import hash_password
from useraccounts.domain.models import Account, Password


class CreateAccountRequestSchema(BaseModel):
    name: str = Field(min_length=1)
    dob: PastDate
    username: str = Field(min_length=4, max_length=50)
    email: EmailStr
    phone_number: Optional[int]
    password: str = Field(min_length=1)

    @validator("phone_number")
    def phone_number_validator(cls, phone_number: str):
        assert len(phone_number) == 10, 'The phone_number must contain 10 digits'
        
        return phone_number
    
    @validator("password")
    def password_validator(cls, password: str):
        return hash_password(password)


    def to_model(self):
        account = Account(
            self.name,
            self.dob,
            self.username,
            self.email,
            self.phone_number
        )
        passowrd = Password(self.password)
        account.password = passowrd

        return account

class AccountMetaSchema(BaseModel):
    account_id: str
    isemail_verified: bool = False
