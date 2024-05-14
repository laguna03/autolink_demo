from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from datetime import datetime


# Create instance of FastAPI
router = APIRouter()

# Establish connection to database
settings = get_settings()
conn = settings
cur = conn.cursor()

# Define models Pydantic for create, read, update, and delete
class Service(BaseModel):
    id: int
    service_name: str
    service_description: str
    service_duration: int
    service_price: float

# CRUD operations for service table

# Create service
@router.post("/services/")
def create_service(service: Service):
    try:
        query = "INSERT INTO service (id, service_name, service_description, service_duration, service_price) VALUES (%s, %s, %s, %s, %s)"
        cur.execute(query, (service.id, service.service_name, service.service_description, service.service_duration, service.service_price))
        conn.commit()
        return {"message": "Work order created successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# Read service
@router.get("/services/{service_id}")
def read_service(service_id: int):
    try:
        query = "SELECT * FROM service WHERE id = %s"
        cur.execute(query, (service_id,))
        service = cur.fetchone()
        if service is None:
            raise HTTPException(status_code=404, detail="Work order not found")
        return service
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# Update service
@router.put("/services/{service_id}")
def update_service(service_id: int, service: Service):
    try:
        query = "UPDATE service SET service_name = %s, service_description = %s, service_duration = %s, service_price = %s WHERE id = %s"
        cur.execute(query, (service.service_name, service.service_description, service.service_duration, service.service_price, service_id))
        conn.commit()
        return {"message": "Work order updated successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# Delete service
@router.delete("/services/{service_id}")
def delete_service(service_id: int):
    try:
        query = "DELETE FROM service WHERE id = %s"
        cur.execute(query, (service_id,))
        conn.commit()
        return {"message": "Work order deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# Close cursor and connection
cur.close()
conn.close()
