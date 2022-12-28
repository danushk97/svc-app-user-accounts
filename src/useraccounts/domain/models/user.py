from uuid import uuid4
from datetime import datetime

from useraccounts.domain.models.password import Password
from useraccounts.domain.models.base_model import BaseModel

class User:
    pass

# class User(BaseModel):
#     def __init__(self,
#         attr: dict,
#         stable_id: str = None,
#         active_flag: bool = True,
#         created_at: datetime = None,
#         created_by: str = None,
#         updated_by: str = None,
#         updated_at: datetime = None
#     ) -> None:
#         super().__init__(
#             active_flag,
#             created_by,
#             created_at,
#             updated_by,
#             updated_at
#         )
#         self.stable_id = stable_id or str(uuid4())
#         self.attr = attr
#         self.passwords = set()
    
#     def set_password(self, password: bytes):
#         return self.passwords.add(password)
