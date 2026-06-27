from fastapi import Depends, Header, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession


from app.db.session import get_db
from app.repositories.tenant import TenantRepository
from app.models.tenant import Tenant
from app.services.tenant import TenantService

from app.config import settings



async def get_tenant_service(db : AsyncSession = Depends(get_db)) -> TenantService:
    return TenantService(db)

async def get_current_tenant(x_api_key: str = Header(..., alias="X-API-Key"), db: AsyncSession = Depends(get_db)) -> Tenant:
    repo = TenantRepository(db)
    tenant = await repo.find_by_api_key(x_api_key)
    if not tenant:
        raise HTTPException(status_code=401, detail="Invalid API key")
    return tenant

async def verify_admin_api_key(x_api_key: str = Header(..., alias="X-API-Key")) -> None:
    if x_api_key != settings.api_key:
        raise HTTPException(status_code=401, detail="Invalid admin API key")
    return None