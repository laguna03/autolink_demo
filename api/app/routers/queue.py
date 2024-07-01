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

@router.post("/queue/add")
async def add_to_queue(item: QueueItem):
    queue.append(item.model_dump())
    return {"message": "Client added to queue"}

@router.post("/queue/add_client")
async def add_to_queue(item: QueueItem):
    client = item.model_dump()
    queue.append(client)
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

