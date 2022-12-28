"""
This module holds request/response schemas for user related endpoints.
"""

from typing import Optional
from pydantic import BaseModel, EmailStr, validator, Field

from useraccounts.schema.post_load_processor import hash_password


class UserAttrSchema(BaseModel):
    email: EmailStr
    phone_number: Optional[int]
    first_name: str = Field(min_length=1)
    last_name: str = Field(min_length=1)
    display_name: str = Field(min_length=5)

    @validator("phone_number")
    def phone_number_validator(cls, phone_number: str):
        assert len(phone_number) == 10, 'The phone_number must contain 10 digits'
        
        return phone_number

class CreateUserRequestSchema(BaseModel):
    attr:  UserAttrSchema
    password: str = Field(min_length=1)

    @validator("password")
    def password_validator(cls, password: str):
        return hash_password(password)
    

class UserIdSchema(BaseModel):
    user_id: str
