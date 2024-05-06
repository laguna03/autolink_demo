from app.models.vehicle_operations import create_vehicle, read_vehicle, update_vehicle, delete_vehicle, VehicleData
from fastapi import APIRouter
from uuid import UUID

router = APIRouter()

@router.post("/vehicles/")
async def create_vehicle_endpoint(vehicle_data: VehicleData) -> dict:
    create_vehicle(vehicle_data)
    return {"message": "Vehicle created successfully"}

@router.get("/vehicles/{vehicle_id}")
async def read_vehicle_endpoint(vehicle_id: UUID) -> VehicleData:
    return read_vehicle(vehicle_id)

@router.put("/vehicles/{vehicle_id}")
async def update_vehicle_endpoint(vehicle_id: UUID, vehicle_data: VehicleData) -> dict:
    update_vehicle(vehicle_id, vehicle_data)
    return {"message": "Vehicle updated successfully"}

@router.delete("/vehicles/{vehicle_id}")
async def delete_vehicle_endpoint(vehicle_id: UUID) -> dict:
    delete_vehicle(vehicle_id)
    return {"message": "Vehicle deleted successfully"}
