from fastapi import HTTPException
from pydantic import BaseModel
from app.services import postgre_connector
from datetime import datetime, date
from uuid import UUID

class VehicleData(BaseModel):
    id: int
    client_id: UUID
    license_plate: str
    vin_number: str
    make: str
    milage: int
    model: str
    year: int


def create_vehicle(vehicle_data):
    conn = postgre_connector.connect_to_database()
    try:
        cur = conn.cursor()
        query = "INSERT INTO vehicles (id, client_id, license_plate, vin_number, make, mileage, model, year) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        cur.execute(query, (
            vehicle_data.id,
            str(vehicle_data.client_id),
            vehicle_data.license_plate,
            vehicle_data.vin_number,
            vehicle_data.make,
            vehicle_data.mileage,
            vehicle_data.model,
            vehicle_data.year
        ))
        conn.commit()
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        cur.close()
        conn.close()


def read_vehicle(vehicle_id):
    conn = postgre_connector.connect_to_database()
    try:
        cur = conn.cursor()
        query = "SELECT * FROM vehicles WHERE id = %s"
        cur.execute(query, (vehicle_id,))
        vehicle = cur.fetchone()
        if vehicle is None:
            raise HTTPException(status_code=404, detail="Vehicle not found")
        return VehicleData(
            id=vehicle[0],
            client_id=UUID(vehicle[1]),
            license_plate=vehicle[2],
            vin_number=vehicle[3],
            make=vehicle[4],
            mileage=vehicle[5],
            model=vehicle[6],
            year=vehicle[7]
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        cur.close()
        conn.close()


def update_vehicle(vehicle_id, vehicle_data):
    conn = postgre_connector.connect_to_database()
    try:
        cur = conn.cursor()
        query = "UPDATE vehicles SET client_id = %s, license_plate = %s, vin_number = %s, make = %s, mileage = %s, model = %s, year = %s WHERE id = %s"
        cur.execute(query, (
            str(vehicle_data.client_id),
            vehicle_data.license_plate,
            vehicle_data.vin_number,
            vehicle_data.make,
            vehicle_data.mileage,
            vehicle_data.model,
            vehicle_data.year,
            vehicle_id
        ))
        conn.commit()
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        cur.close()
        conn.close()


def delete_vehicle(vehicle_id):
    conn = postgre_connector.connect_to_database()
    try:
        cur = conn.cursor()
        query = "DELETE FROM vehicles WHERE id = %s"
        cur.execute(query, (vehicle_id,))
        conn.commit()
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        cur.close()
        conn.close()
