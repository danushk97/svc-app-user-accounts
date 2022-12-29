from datetime import datetime
from uuid import UUID


class BaseModel:
    def __init__(self,
        created_by: str,
        created_at: datetime, 
        updated_by: UUID,
        updated_at: datetime
    ) -> None:
        self.created_by = created_by
        self.created_at = created_at
        self.updated_by = updated_by
        self.updated_at = updated_at
        