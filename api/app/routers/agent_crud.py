from app.models.agent_operations import create_agent, read_agent, update_agent, delete_agent, AgentData
from fastapi import APIRouter
from uuid import UUID
from typing import List, Optional
router = APIRouter()

@router.post("/")
async def create_agent_endpoint(agent_data: AgentData) -> dict:
    create_agent(agent_data)
    return {"message": "Agent created successfully"}

@router.get("/")
async def read_agent_endpoint(agent_id: Optional[UUID] = None, first_name: Optional[str] = None, last_name: Optional[str] = None, email: Optional[str] = None, employee_num: Optional[str] = None) -> List[AgentData]:
    return read_agent(agent_id=agent_id, first_name=first_name, last_name=last_name, email=email, employee_num=employee_num)


@router.put("/{agent_id}")
async def update_agent_endpoint(agent_id: UUID, agent_data: AgentData) -> dict:
    update_agent(agent_id, agent_data)
    return {"message": "Agent updated successfully"}

@router.delete("/{agent_id}")
async def delete_agent_endpoint(agent_id: UUID) -> dict:
    delete_agent(agent_id)
    return {"message": "Agent deleted successfully"}
