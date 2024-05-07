from fastapi import HTTPException
from pydantic import BaseModel
from app.services import postgre_connector
from datetime import datetime
from uuid import UUID


class AgentData(BaseModel):
    id: UUID
    updated_at: datetime
    first_name: str
    last_name: str
    email: str
    employee_num: str


def create_agent(agent_data: AgentData):
    conn = postgre_connector.connect_to_database()
    try:
        cur = conn.cursor()
        query = "INSERT INTO agents (id, updated_at, first_name, last_name, email, employee_num) VALUES (%s, %s, %s, %s, %s, %s)"
        cur.execute(query, (
            str(agent_data.id),
            agent_data.updated_at,
            agent_data.first_name,
            agent_data.last_name,
            agent_data.email,
            agent_data.employee_num
        ))
        conn.commit()
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        cur.close()
        conn.close()


def read_agent(agent_id: UUID) -> AgentData:
    conn = postgre_connector.connect_to_database()
    try:
        cur = conn.cursor()
        query = "SELECT * FROM agents WHERE id = %s"
        cur.execute(query, (str(agent_id),))
        agent = cur.fetchone()
        if agent is None:
            raise HTTPException(status_code=404, detail="Agent not found")
        return AgentData(
            id=agent[0],
            updated_at=agent[1],
            first_name=agent[2],
            last_name=agent[3],
            email=agent[4],
            employee_num=agent[5]
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        cur.close()
        conn.close()


def update_agent(agent_id: UUID, agent_data: AgentData):
    conn = postgre_connector.connect_to_database()
    try:
        cur = conn.cursor()
        query = "UPDATE agents SET updated_at = %s, first_name = %s, last_name = %s, email = %s, employee_num = %s WHERE id = %s"
        cur.execute(query, (
            agent_data.updated_at,
            agent_data.first_name,
            agent_data.last_name,
            agent_data.email,
            agent_data.employee_num,
            str(agent_id)
        ))
        conn.commit()
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        cur.close()
        conn.close()


def delete_agent(agent_id: UUID):
    conn = postgre_connector.connect_to_database()
    try:
        cur = conn.cursor()
        query = "DELETE FROM agents WHERE id = %s"
        cur.execute(query, (str(agent_id),))
        conn.commit()
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        cur.close()
        conn.close()
