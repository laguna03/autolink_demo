from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import psycopg2
import uuid
from datetime import datetime, date
from app.settings.application import get_settings
from app.settings.logger import get_logger

# Create instance of FastAPI
router = APIRouter()

# Define models Pydantic for create, read, update, and delete
class Agent(BaseModel):
    id: uuid.UUID
    updated_at: datetime
    first_name: str
    last_name: str
    email: str
    employee_num: str

# CRUD operations for agent table

# Create agent
@router.post("/agents/")
def create_agent(agent: Agent):
    try:
        settings = get_settings()
        conn = settings
        cur = conn.cursor()

        query = "INSERT INTO agent (id, updated_at, first_name, last_name, email, employee_num) VALUES (%s, %s, %s, %s, %s, %s)"
        cur.execute(query, (agent.id, agent.updated_at, agent.first_name, agent.last_name, agent.email, agent.employee_num))
        conn.commit()
        return {"message": "Agent created successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        cur.close()
        conn.close()

# Read agent
@router.get("/agents/{agent_id}")
def read_agent(agent_id: uuid.UUID):
    try:
        settings = get_settings()
        conn = settings
        cur = conn.cursor()

        query = "SELECT * FROM agent WHERE id = %s"
        cur.execute(query, (agent_id,))
        agent = cur.fetchone()
        if agent is None:
            raise HTTPException(status_code=404, detail="Agent not found")
        return agent
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        cur.close()
        conn.close()

# Update agent
@router.put("/agents/{agent_id}")
def update_agent(agent_id: uuid.UUID, agent: Agent):
    try:
        settings = get_settings()
        conn = settings
        cur = conn.cursor()

        query = "UPDATE agent SET updated_at = %s, first_name = %s, last_name = %s, email = %s, employee_num = %s WHERE id = %s"
        cur.execute(query, (agent.updated_at, agent.first_name, agent.last_name, agent.email, agent.employee_num, agent_id))
        conn.commit()
        return {"message": "Agent updated successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        cur.close()
        conn.close()

# Delete agent
@router.delete("/agents/{agent_id}")
def delete_agent(agent_id: uuid.UUID):
    try:
        settings = get_settings()
        conn = settings
        cur = conn.cursor()

        query = "DELETE FROM agent WHERE id = %s"
        cur.execute(query, (agent_id,))
        conn.commit()
        return {"message": "Agent deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        cur.close()
        conn.close()
