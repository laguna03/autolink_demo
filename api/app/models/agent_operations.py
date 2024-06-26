from fastapi import HTTPException
from app.services import postgre_connector
from uuid import UUID
from typing import List, Optional
from .classes.agent_class import AgentData


def create_agent(agent_data: AgentData):
    conn = postgre_connector.connect_to_database()
    try:
        cur = conn.cursor()
        query = "INSERT INTO autolink.agents (agent_id, updated_at, first_name, last_name, username, hashed_password, email) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        cur.execute(query, (
            str(agent_data.agent_id),
            agent_data.updated_at,
            agent_data.first_name,
            agent_data.last_name,
            agent_data.username,
            agent_data.hashed_password,
            agent_data.email,
        ))
        conn.commit()
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        cur.close()
        conn.close()


def read_agent(agent_id: Optional[UUID] = None, first_name: Optional[str] = None, last_name: Optional[str] = None, email: Optional[str] = None, employee_num: Optional[str] = None) -> List[AgentData]:
    # Create a list to store conditions for the WHERE clause
    conditions = []
    params = []

    # Check each parameter and add condition to the list if not None
    if agent_id:
        conditions.append("id = %s")
        params.append(str(agent_id))
    if first_name:
        conditions.append("first_name = %s")
        params.append(first_name)
    if last_name:
        conditions.append("last_name = %s")
        params.append(last_name)
    if email:
        conditions.append("email = %s")
        params.append(email)
    if employee_num:
        conditions.append("employee_num = %s")
        params.append(employee_num)

    # Join conditions with 'AND' and create the WHERE clause
    where_clause = " AND ".join(conditions)

    # Connect to the database
    conn = postgre_connector.connect_to_database()
    try:
        cur = conn.cursor()
        query = "SELECT * FROM agents"
        if where_clause:
            query += " WHERE " + where_clause
        cur.execute(query, tuple(params))
        agents = cur.fetchall()
        if not agents:
            raise HTTPException(status_code=404, detail="Agents not found")
        return [AgentData(
            id=agent[0],
            updated_at=agent[1],
            first_name=agent[2],
            last_name=agent[3],
            email=agent[4],
            employee_num=agent[5]
        ) for agent in agents]
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
