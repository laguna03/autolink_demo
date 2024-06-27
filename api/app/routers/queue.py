from fastapi import APIRouter, HTTPException
from typing import List
from pydantic import BaseModel
from app.services.postgre_connector import connect_to_database, close_connection
import psycopg2

router = APIRouter()


class QueueItem(BaseModel):
    name: str

class AddQueueItem(BaseModel):
    name: str

@router.get("/queue", response_model=List[QueueItem])
def get_clients_from_db():
    conn = connect_to_database()
    if conn is None:
        raise HTTPException(status_code=500, detail="Error connecting to the database")

    try:
        cur = conn.cursor()
        cur.execute("SELECT first_name FROM autolink.clients")
        rows = cur.fetchall()
        return [QueueItem(name=row[0]) for row in rows]
    except (Exception, psycopg2.Error) as error:
        print("Error fetching data from PostgreSQL:", error)
        raise HTTPException(status_code=500, detail="Error fetching data from the database")
    finally:
        close_connection(conn)

# Endpoint para obtener la cola
@router.get("/queue", response_model=List[QueueItem])
async def get_queue():
    queue_data = get_clients_from_db()
    return queue_data

@router.delete("/{item_name}")
async def delete_queue_item(item_name: str):
    conn = connect_to_database()
    if conn is None:
        raise HTTPException(status_code=500, detail="Error connecting to the database")

    try:
        cur = conn.cursor()
        cur.execute("DELETE FROM autolink.clients WHERE first_name = %s", (item_name,))
        conn.commit()
        return {"message": f"Item '{item_name}' removed successfully"}
    except (Exception, psycopg2.Error) as error:
        print("Error deleting data from PostgreSQL:", error)
        raise HTTPException(status_code=500, detail="Error deleting data from the database")
    finally:
        close_connection(conn)

@router.post("/add")
async def add_to_queue(item: AddQueueItem):
    conn = connect_to_database()
    if conn is not None:
        try:
            cur = conn.cursor()
            # query = "SELECT FROM autolink.clients WHERE first_name = %s"
            cur.execute("SELECT FROM autolink.clients WHERE first_name = %s", (item.name,))
            conn.commit()
            return {"message": f"Client {item.name} added to the queue"}
        except (Exception, psycopg2.Error) as error:
            print("Error while adding to queue:", error)
            raise HTTPException(status_code=500, detail="Error while adding to queue")
        finally:
            cur.close()
            close_connection(conn)
    else:
        raise HTTPException(status_code=500, detail="Database connection failed")