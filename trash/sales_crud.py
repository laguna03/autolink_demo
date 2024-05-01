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
class Sale(BaseModel):
    id: int
    service_id: int
    agent_id: uuid.UUID
    status: str
    updated_at: datetime
    final_price: float

# CRUD operations for sale table

# Create sale
@router.post("/sales/")
def create_sale(sale: Sale):
    try:
        query = "INSERT INTO sale (id, service_id, agent_id, status, updated_at, final_price) VALUES (%s, %s, %s, %s, %s, %s)"
        cur.execute(query, (sale.id, sale.service_id, sale.agent_id, sale.status, sale.updated_at, sale.final_price))
        conn.commit()
        return {"message": "Invoice created successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# Read sale
@router.get("/sales/{sale_id}")
def read_sale(sale_id: int):
    try:
        query = "SELECT * FROM sale WHERE id = %s"
        cur.execute(query, (sale_id,))
        sale = cur.fetchone()
        if sale is None:
            raise HTTPException(status_code=404, detail="Invoice not found")
        return sale
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# Update sale
@router.put("/sales/{sale_id}")
def update_sale(sale_id: int, sale: Sale):
    try:
        query = "UPDATE sale SET service_id = %s, agent_id = %s, status = %s, updated_at = %s, final_price = %s WHERE id = %s"
        cur.execute(query, (sale.service_id, sale.agent_id, sale.status, sale.updated_at, sale.final_price, sale_id))
        conn.commit()
        return {"message": "Invoice updated successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# Delete sale
@router.delete("/sales/{sale_id}")
def delete_sale(sale_id: int):
    try:
        query = "DELETE FROM sale WHERE id = %s"
        cur.execute(query, (sale_id,))
        conn.commit()
        return {"message": "Invoice deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# Close cursor and connection
cur.close()
conn.close()
