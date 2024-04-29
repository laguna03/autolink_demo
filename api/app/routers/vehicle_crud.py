from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import psycopg2
import uuid
from datetime import datetime
from app.settings.application import get_settings

# Create instance of FastAPI
router = APIRouter()

# Establish connection to database
settings = get_settings()
conn = settings
cur = conn.cursor()

# Define models Pydantic for create, read, update, and delete
class Vehicle(BaseModel):
    id: int
    client_id: uuid.UUID
    license_plate: str
    vin_number: str
    make: str
    milage: int
    model: str
    year: int

# CRUD operations for vehicle table

# Create vehicle
@router.post("/vehicles/")
def create_vehicle(vehicle: Vehicle):
    try:
        query = "INSERT INTO vehicle (id, client_id, license_plate, vin_number, make, milage, model, year) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        cur.execute(query, (vehicle.id, vehicle.client_id, vehicle.license_plate, vehicle.vin_number, vehicle.make, vehicle.milage, vehicle.model, vehicle.year))
        conn.commit()
        return {"message": "Vehicle created successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# Read vehicle
@router.get("/vehicles/{vehicle_id}")
def read_vehicle(vehicle_id: int):
    try:
        query = "SELECT * FROM vehicle WHERE id = %s"
        cur.execute(query, (vehicle_id,))
        vehicle = cur.fetchone()
        if vehicle is None:
            raise HTTPException(status_code=404, detail="Vehicle not found")
        return vehicle
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# Update vehicle
@router.put("/vehicles/{vehicle_id}")
def update_vehicle(vehicle_id: int, vehicle: Vehicle):
    try:
        query = "UPDATE vehicle SET client_id = %s, license_plate = %s, vin_number = %s, make = %s, milage = %s, model = %s, year = %s WHERE id = %s"
        cur.execute(query, (vehicle.client_id, vehicle.license_plate, vehicle.vin_number, vehicle.make, vehicle.milage, vehicle.model, vehicle.year, vehicle_id))
        conn.commit()
        return {"message": "Vehicle updated successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# Delete vehicle
@router.delete("/vehicles/{vehicle_id}")
def delete_vehicle(vehicle_id: int):
    try:
        query = "DELETE FROM vehicle WHERE id = %s"
        cur.execute(query, (vehicle_id,))
        conn.commit()
        return {"message": "Vehicle deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# Close cursor and connection
cur.close()
conn.close()
