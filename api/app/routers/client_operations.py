from app.models.client_crud import create_client, read_client, update_client, delete_client, ClientData
from fastapi import APIRouter
from uuid import UUID


router = APIRouter()

@router.post("/clients/")
async def create_client_endpoint(client_data: ClientData) -> dict:
    create_client(client_data)
    return {"message": "Client created successfully"}

@router.get("/clients/{client_id}")
async def read_client_endpoint(client_id: UUID) -> ClientData:
    return read_client(client_id)

@router.put("/clients/{client_id}")
async def update_client_endpoint(client_id: UUID, client_data: ClientData) -> dict:
    update_client(client_id, client_data)
    return {"message": "Client updated successfully"}

@router.delete("/clients/{client_id}")
async def delete_client_endpoint(client_id: UUID) -> dict:
    delete_client(client_id)
    return {"message": "Client deleted successfully"}
