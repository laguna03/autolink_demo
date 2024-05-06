from app.models.service_operations import create_service, read_service, update_service, delete_service, ServiceData
from fastapi import APIRouter
from uuid import UUID

router = APIRouter()

@router.post("/services/")
async def create_service_endpoint(service_data: ServiceData) -> dict:
    create_service(service_data)
    return {"message": "Service created successfully"}

@router.get("/services/{service_id}")
async def read_service_endpoint(service_id: UUID) -> ServiceData:
    return read_service(service_id)

@router.put("/services/{service_id}")
async def update_service_endpoint(service_id: UUID, service_data: ServiceData) -> dict:
    update_service(service_id, service_data)
    return {"message": "Service updated successfully"}

@router.delete("/services/{service_id}")
async def delete_service_endpoint(service_id: UUID) -> dict:
    delete_service(service_id)
    return {"message": "Service deleted successfully"}
