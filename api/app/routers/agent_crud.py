from app.models.agent_operations import create_agent, read_agent, update_agent, delete_agent, AgentData
from fastapi import APIRouter
from uuid import UUID

router = APIRouter()

@router.post("/")
async def create_agent_endpoint(agent_data: AgentData) -> dict:
    create_agent(agent_data)
    return {"message": "Agent created successfully"}

@router.get("/{agent_id}")
async def read_agent_endpoint(agent_id: UUID) -> AgentData:
    return read_agent(agent_id)

@router.put("/{agent_id}")
async def update_agent_endpoint(agent_id: UUID, agent_data: AgentData) -> dict:
    update_agent(agent_id, agent_data)
    return {"message": "Agent updated successfully"}

@router.delete("/{agent_id}")
async def delete_agent_endpoint(agent_id: UUID) -> dict:
    delete_agent(agent_id)
    return {"message": "Agent deleted successfully"}
