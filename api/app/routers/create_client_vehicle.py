from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from uuid import UUID
from app.models.client_operations import create_client
from app.models.vehicle_operations import create_vehicle
from app.models.classes.client_class import ClientData
from app.models.classes.vehicle_class import VehicleData
from app.models.classes.appointment_class import AppointmentData
from app.models.appointment_operations import create_appointment
from app.routers.queue import add_to_queue, QueueItem, queue

router = APIRouter()

class ClientAndVehicleData(BaseModel):
    client_data: ClientData
    vehicle_data: VehicleData

@router.post("/create-client")
async def create_client_and_vehicle(data: ClientAndVehicleData):
    try:
        create_client(data.client_data)
        create_vehicle(data.vehicle_data)
        # Add the new client to the queue
        queue_item = QueueItem(
            name=data.client_data.first_name,
            model=data.vehicle_data.model,
            license_plate=data.vehicle_data.license_plate
        )
        queue.append(queue_item.model_dump())  # Añadir directamente a la lista de queue
        return {"message": "Client and vehicle created successfully",
                "client_id": data.client_data.client_id,
                "vehicle_id": data.vehicle_data.vehicle_id}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# @router.post("/create-appointment")
# async def create_appointment_endpoint(appointment_data: AppointmentData) -> dict:
#     create_appointment(appointment_data)
#     return {"message": "Appointment created successfully"}

