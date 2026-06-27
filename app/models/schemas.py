from pydantic import BaseModel
from uuid import UUID
from datetime import datetime

class TenantResponse(BaseModel):
    id: UUID
    name: str
    api_key: str
    created_at: datetime

class TenantCreate(BaseModel):
    name: str