from pydantic import BaseModel
from sqlmodel import Field, SQLModel
from datetime import datetime
from uuid import UUID, uuid4

class Tenant(SQLModel, table=True):
    __tablename__ = "tenants"
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    name: str
    api_key: str
    created_at: datetime = Field(default_factory=datetime.now)