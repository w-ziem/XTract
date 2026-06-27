from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.tenant import TenantRepository
from app.models.tenant import Tenant
import secrets

class TenantService:
    def __init__(self, session: AsyncSession):
        self.repo = TenantRepository(session)

    async def create_tenant(self, tenant_name: str) -> Tenant:
        
        
        API_KEY = "xtract-" + secrets.token_hex(32)
        tenant = Tenant(name=tenant_name, api_key=API_KEY)
        return await self.repo.save(tenant)