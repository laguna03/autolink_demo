from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import psycopg2
import uuid
from datetime import datetime, date
from app.settings.application import get_settings

# Create instance of FastAPI
router = APIRouter()

# Define models Pydantic for create, read, update and delete
class Appointment(BaseModel):
    id: int
    agent_id: uuid.UUID
    sale_id: int
    client_id: uuid.UUID
    service_id: int
    vehicule_id: int
    created_at: datetime
    status: str
    appt_time: date

# CRUD operations for appointment table

# Create appointment
@router.post("/appointments/")
def create_appointment(appointment: Appointment):
    try:
        settings = get_settings()
        conn = settings
        cur = conn.cursor()

        query = "INSERT INTO appointment (id, agent_id, sale_id, client_id, service_id, vehicule_id, created_at, status, appt_time) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        cur.execute(query, (appointment.id, appointment.agent_id, appointment.sale_id, appointment.client_id, appointment.service_id, appointment.vehicule_id, appointment.created_at, appointment.status, appointment.appt_time))
        conn.commit()
        return {"message": "Appointment created successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        cur.close()
        conn.close()

# Read appointment
@router.get("/appointments/{appointment_id}")
def read_appointment(appointment_id: int):
    try:
        settings = get_settings()
        conn = settings
        cur = conn.cursor()

        query = "SELECT * FROM appointment WHERE id = %s"
        cur.execute(query, (appointment_id,))
        appointment = cur.fetchone()
        if appointment is None:
            raise HTTPException(status_code=404, detail="Appointment not found")
        return appointment
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        cur.close()
        conn.close()

# Update appointment
@router.put("/appointments/{appointment_id}")
def update_appointment(appointment_id: int, appointment: Appointment):
    try:
        settings = get_settings()
        conn = settings
        cur = conn.cursor()

        query = "UPDATE appointment SET agent_id = %s, sale_id = %s, client_id = %s, service_id = %s, vehicule_id = %s, created_at = %s, status = %s, appt_time = %s WHERE id = %s"
        cur.execute(query, (appointment.agent_id, appointment.sale_id, appointment.client_id, appointment.service_id, appointment.vehicule_id, appointment.created_at, appointment.status, appointment.appt_time, appointment_id))
        conn.commit()
        return {"message": "Appointment updated successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        cur.close()
        conn.close()

# Delete appointment
@router.delete("/appointments/{appointment_id}")
def delete_appointment(appointment_id: int):
    try:
        settings = get_settings()
        conn = settings
        cur = conn.cursor()

        query = "DELETE FROM appointment WHERE id = %s"
        cur.execute(query, (appointment_id,))
        conn.commit()
        return {"message": "Appointment deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        cur.close()
        conn.close()
