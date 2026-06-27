from fastapi import APIRouter, Depends, HTTPException
from app.models.schemas import TenantCreate, TenantResponse
from app.services.tenant import TenantService
from app.deps import get_tenant_service, verify_admin_api_key

router = APIRouter(prefix="admin", tags=["admin"])

@router.post("/tenants", response_model=TenantResponse, status_code=201)
async def create_tenant(
        request: TenantCreate, 
        _: None = Depends(verify_admin_api_key),
        tenant_service: TenantService = Depends(get_tenant_service)
        ) -> TenantResponse:
    return await tenant_service.create_tenant(request.name)