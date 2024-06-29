from fastapi import APIRouter, HTTPException
from typing import List, Dict
from pydantic import BaseModel
from app.services.postgre_connector import connect_to_database, close_connection

router = APIRouter()

class QueueItem(BaseModel):
    name: str
    model: str
    license_plate: str

queue = []
ongoing_services = []

@router.get("/queue")
async def get_queue():
    conn = connect_to_database()
    try:
        cur = conn.cursor()
        query = """
            SELECT c.first_name, v.model, v.license_plate
            FROM autolink.clients AS c
            JOIN autolink.vehicles AS v ON c.client_id = v.client_id
            """
        cur.execute(query)
        rows = cur.fetchall()
        queue_items = [
            QueueItem(name=row[0], model=row[1], license_plate=row[2]).model_dump()
            for row in rows
        ]
        return {"queue": queue_items, "ongoingServices": ongoing_services}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cur.close()
        conn.close()

# Still adjusting function
@router.post("/queue/add")
def add_to_queue(item: QueueItem):
    queue.append(item.model_dump())
    item_dict = item.model_dump()
    if item_dict in queue:
        queue.remove(item_dict)
        ongoing_services.append(item_dict)
    return {"message": "Client added to queue"}

@router.post("/queue/start_service")
async def start_service(item: QueueItem):
    add_to_queue(item)
    item_dict = item.model_dump()
    if item_dict in queue:
        queue.remove(item_dict)
        ongoing_services.append(item_dict)
        return {"message": "Service started"}
    raise HTTPException(status_code=404, detail="Client not found in queue")

@router.delete("/queue/{name}")
async def delete_from_queue(name: str):
    global queue, ongoing_services
    queue = [item for item in queue if item['name'] != name]
    ongoing_services = [item for item in ongoing_services if item['name'] != name]
    return {"message": f"Client {name} removed from queue"}
