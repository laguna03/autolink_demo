from fastapi import HTTPException
from pydantic import BaseModel
from app.services import postgre_connector
from datetime import datetime, date
from uuid import UUID

class ClientData(BaseModel):
    id: UUID
    updated_at: datetime
    first_name: str
    last_name: str
    email: str
    phone: str
    date_of_birth: date


def create_client(client_data):
    conn = postgre_connector.connect_to_database()
    try:
        cur = conn.cursor()
        query = "INSERT INTO clients (id, updated_at, first_name, last_name, email, phone, date_of_birth) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        cur.execute(query, (
            str(client_data.id),
            client_data.updated_at,
            client_data.first_name,
            client_data.last_name,
            client_data.email,
            client_data.phone,
            client_data.date_of_birth
        ))
        conn.commit()
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        cur.close()
        conn.close()


def read_client(client_id):
    conn = postgre_connector.connect_to_database()
    try:
        cur = conn.cursor()
        query = "SELECT * FROM clients WHERE id = %s"
        cur.execute(query, (str(client_id),))
        client = cur.fetchone()
        if client is None:
            raise HTTPException(status_code=404, detail="Client not found")
        return ClientData(
            id=client[0],
            updated_at=client[1],
            first_name=client[2],
            last_name=client[3],
            email=client[4],
            phone=client[5],
            date_of_birth=client[6]
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        cur.close()
        conn.close()


def update_client(client_id, client_data):
    conn = postgre_connector.connect_to_database()
    try:
        cur = conn.cursor()
        query = "UPDATE clients SET updated_at = %s, first_name = %s, last_name = %s, email = %s, phone = %s, date_of_birth = %s WHERE id = %s"
        cur.execute(query, (
            client_data.updated_at,
            client_data.first_name,
            client_data.last_name,
            client_data.email,
            client_data.phone,
            client_data.date_of_birth,
            str(client_id)
        ))
        conn.commit()
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        cur.close()
        conn.close()


def delete_client(client_id):
    conn = postgre_connector.connect_to_database()
    try:
        cur = conn.cursor()
        query = "DELETE FROM clients WHERE id = %s"
        cur.execute(query, (str(client_id),))
        conn.commit()
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        cur.close()
        conn.close()