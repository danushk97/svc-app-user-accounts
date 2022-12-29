"""
This module holds request/response schemas for user related endpoints.
"""

from typing import Optional
from pydantic import BaseModel, EmailStr, validator, Field

from useraccounts.schemas.post_load_processor import hash_password


class AccountAttrSchema(BaseModel):
    phone_number: Optional[int]
    name: str = Field(min_length=1)

    @validator("phone_number")
    def phone_number_validator(cls, phone_number: str):
        assert len(phone_number) == 10, 'The phone_number must contain 10 digits'
        
        return phone_number


class CreateAccountRequestSchema(BaseModel):
    username: str = Field(min_length=4, max_length=50)
    email: EmailStr
    attr:  AccountAttrSchema
    password: str = Field(min_length=1)

    @validator("password")
    def password_validator(cls, password: str):
        return hash_password(password)


class AccountMetaSchema(BaseModel):
    account_id: str
    isemail_verified: bool = False
