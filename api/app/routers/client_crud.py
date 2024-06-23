from app.models.client_operations import create_client, read_client, update_client, delete_client, ClientData, ClientResponse, get_clients_data
from fastapi import APIRouter, HTTPException
from uuid import UUID
from typing import List, Dict



router = APIRouter()

@router.post("/")
async def create_client_endpoint(client_data: ClientData) -> dict:
    create_client(client_data)
    return {"message": "Client created successfully"}

@router.get("/")
async def read_client_endpoint(client_id: UUID = None, first_name: str = None, last_name: str = None, email: str = None, phone: str = None) -> List[ClientResponse]:
    return read_client(client_id=client_id, first_name=first_name, last_name=last_name, email=email, phone=phone)

@router.put("/{client_id}")
async def update_clients_endpoint(client_id: UUID = None, first_name: str = None, last_name: str = None, email: str = None, phone: str = None, client_data: ClientData = None) -> dict:
    # Ensure that the client ID provided in the path matches the client ID in the request body
    if client_id != client_data.id:
        raise HTTPException(status_code=400, detail="Client ID in path does not match client ID in request body")
    # Update the client
    update_client(client_id, client_data)
    return {"message": "Client updated successfully"}

@router.delete("/{client_id}")
async def delete_client_endpoint(client_id: UUID = None, first_name: str = None, last_name: str = None, email: str = None, phone: str = None, client_data: ClientData = None) -> dict:
    delete_client(client_id)
    return {"message": "Client deleted successfully"}

@router.get("/dashboard-data")
async def get_dashboard_data_endpoint() -> List[Dict[str, str]]:
    data = get_clients_data()
    if data:
        return data
    else:
        raise HTTPException(status_code=500, detail="Error al obtener datos")