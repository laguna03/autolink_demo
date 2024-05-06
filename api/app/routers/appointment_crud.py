from app.models.appointment_operations import create_appointment, read_appointment, update_appointment, delete_appointment, AppointmentData
from fastapi import APIRouter
from uuid import UUID


router = APIRouter()

@router.post("/appointments/")
async def create_appointment_endpoint(appointment_data: AppointmentData) -> dict:
    create_appointment(appointment_data)
    return {"message": "Appointment created successfully"}

@router.get("/appointments/{appointment_id}")
async def read_appointment_endpoint(appointment_id: int) -> AppointmentData:
    return read_appointment(appointment_id)

@router.put("/appointments/{appointment_id}")
async def update_appointment_endpoint(appointment_id: int, appointment_data: AppointmentData) -> dict:
    update_appointment(appointment_id, appointment_data)
    return {"message": "Appointment updated successfully"}

@router.delete("/appointments/{appointment_id}")
async def delete_appointment_endpoint(appointment_id: int) -> dict:
    delete_appointment(appointment_id)
    return {"message": "Appointment deleted successfully"}
