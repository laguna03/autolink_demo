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
    return {"queue": queue, "ongoingServices": ongoing_services}

# @router.get("/queue")
# async def get_queue():
#     global queue  # Usar la variable global queue
#     conn = connect_to_database()
#     try:
#         cur = conn.cursor()
#         query = """
#             SELECT c.first_name, v.model, v.license_plate
#             FROM autolink.clients AS c
#             JOIN autolink.vehicles AS v ON c.client_id = v.client_id
#             """
#         cur.execute(query)
#         rows = cur.fetchall()
#         queue.clear()  # Limpiar la lista antes de llenarla de nuevo
#         for row in rows:
#             queue.append(QueueItem(name=row[0], model=row[1], license_plate=row[2]).model_dump())
#         return {"queue": queue, "ongoingServices": ongoing_services}
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))
#     finally:
#         cur.close()
#         conn.close()

# Still adjusting function
@router.post("/queue/add")
async def add_to_queue(item: QueueItem):
    queue.append(item.model_dump())
    return {"message": "Client added to queue"}

@router.post("/start_service")
async def start_service(item: QueueItem):
    item_dict = item.model_dump()
    if item_dict in queue:
        ongoing_services.append(item_dict)
        queue.remove(item_dict)
        return {"message": "Service started"}
    raise HTTPException(status_code=404, detail="Client not found in queue")

@router.delete("/queue/{name}")
async def delete_from_queue(name: str):
    global queue, ongoing_services
    queue = [item for item in queue if item['name'] != name]
    ongoing_services = [item for item in ongoing_services if item['name'] != name]
    return {"message": f"Client {name} removed from queue"}

