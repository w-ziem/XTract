from sqlmodel import AsyncSession
from app.models.tenant import Tenant
from uuid import UUID

class TenantRepository:
    def __init__(self, session: AsyncSession):
        self.session = session
    
    async def find_by_id(self, id: UUID) -> Tenant | None:
        return await self.session.get(Tenant, id)

    async def find_by_api_key(self, api_key: str) -> Tenant | None:
        result = await self.session.execute(select(Tenant).where(Tenant.api_key == api_key))
        return result.scalar_one_or_none()

    async def save(self, tenant: Tenant) -> Tenant:
        self.session.add(tenant)
        await self.session.commit()
        await self.session.refresh(tenant)
        return tenant

    async def delete(self, id: UUID) -> None:
        tenant = await self.find_by_id(id)
        if tenant:
            await self.session.delete(tenant)
            await self.session.commit()