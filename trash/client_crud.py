from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import psycopg2
import uuid
from datetime import datetime, date
from app.settings.application import get_settings

# Create instance of FastAPI
router = APIRouter()

# Establish connection to database
settings = get_settings()
conn = settings
cur = conn.cursor()

# Define models Pydantic for create, read, update, and delete
class Client(BaseModel):
    id: uuid.UUID
    updated_at: datetime
    first_name: str
    last_name: str
    email: str
    phone: str
    date_of_birth: date

# CRUD operations for client table

# Create client
@router.post("/clients/")
def create_client(client: Client):
    try:
        query = "INSERT INTO client (id, updated_at, first_name, last_name, email, phone, date_of_birth) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        cur.execute(query, (client.id, client.updated_at, client.first_name, client.last_name, client.email, client.phone, client.date_of_birth))
        conn.commit()
        return {"message": "Client created successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# Read client
@router.get("/clients/{client_id}")
def read_client(client_id: uuid.UUID):
    try:
        query = "SELECT * FROM client WHERE id = %s"
        cur.execute(query, (client_id,))
        client = cur.fetchone()
        if client is None:
            raise HTTPException(status_code=404, detail="Client not found")
        return client
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# Update client
@router.put("/clients/{client_id}")
def update_client(client_id: uuid.UUID, client: Client):
    try:
        query = "UPDATE client SET updated_at = %s, first_name = %s, last_name = %s, email = %s, phone = %s, date_of_birth = %s WHERE id = %s"
        cur.execute(query, (client.updated_at, client.first_name, client.last_name, client.email, client.phone, client.date_of_birth, client_id))
        conn.commit()
        return {"message": "Client updated successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# Delete client
@router.delete("/clients/{client_id}")
def delete_client(client_id: uuid.UUID):
    try:
        query = "DELETE FROM client WHERE id = %s"
        cur.execute(query, (client_id,))
        conn.commit()
        return {"message": "Client deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# Close cursor and connection
cur.close()
conn.close()
