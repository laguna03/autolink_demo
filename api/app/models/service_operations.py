from fastapi import HTTPException
from pydantic import BaseModel
from app.services import postgre_connector
from datetime import datetime, date
from uuid import UUID

class ServiceData(BaseModel):
    id: int
    service_name: str
    service_description: str
    service_duration: int
    service_price: float

def create_service(service_data):
    conn = postgre_connector.connect_to_database()
    try:
        cur = conn.cursor()
        query = "INSERT INTO services (id, service_name, service_description, service_duration, service_price) VALUES (%s, %s, %s, %s, %s)"
        cur.execute(query, (
            service_data.id,
            service_data.service_name,
            service_data.service_description,
            service_data.service_duration,
            service_data.service_price
        ))
        conn.commit()
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        cur.close()
        conn.close()

def read_service(service_id):
    conn = postgre_connector.connect_to_database()
    try:
        cur = conn.cursor()
        query = "SELECT * FROM services WHERE id = %s"
        cur.execute(query, (service_id,))
        service = cur.fetchone()
        if service is None:
            raise HTTPException(status_code=404, detail="Service not found")
        return ServiceData(
            id=service[0],
            service_name=service[1],
            service_description=service[2],
            service_duration=service[3],
            service_price=service[4]
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        cur.close()
        conn.close()

def update_service(service_id, service_data):
    conn = postgre_connector.connect_to_database()
    try:
        cur = conn.cursor()
        query = "UPDATE services SET service_name = %s, service_description = %s, service_duration = %s, service_price = %s WHERE id = %s"
        cur.execute(query, (
            service_data.service_name,
            service_data.service_description,
            service_data.service_duration,
            service_data.service_price,
            service_id
        ))
        conn.commit()
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        cur.close()
        conn.close()

def delete_service(service_id):
    conn = postgre_connector.connect_to_database()
    try:
        cur = conn.cursor()
        query = "DELETE FROM services WHERE id = %s"
        cur.execute(query, (service_id,))
        conn.commit()
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        cur.close()
        conn.close()
