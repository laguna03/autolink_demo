from fastapi import FastAPI
from pydantic import BaseModel
import psycopg2
import uuid
from datetime import datetime, date

# Create instance of FastAPI
app = FastAPI()

# Establish connection to database
conn = psycopg2.connect(
    dbname="autolinkdb",
    user="pedrolaguna",
    password="autolink2024",
    host="localhost",
    port="5432"
)

#create cursor to execute consults
cur = conn.cursor()

#Define models Pydantic for create, read, update and delete
class Agent(BaseModel):
    id: uuid
    updated_at: datetime
    first_name: str
    last_name: str
    email: str
    employee_num: str

#CRUD operations for agent table

#Create agent
@app.post("/agents/")
def create_agent(agent: Agent):
    query = "INSERT INTO agent (id, updated_at, first_name, last_name, email, employee_num) VALUES (%s, %s, %s, %s, %s, %s)"
    cur.execute(query, (agent.id, agent.updated_at, agent.first_name, agent.last_name, agent.email, agent.employee_num))
    conn.commit()
    return {"message": "Agent created successfully"}

#Read agent
@app.get("/agents/{agent_id}")
def read_agent(agent_id: uuid):
    query = "SELECT * FROM agent WHERE id = %s"
    cur.execute(query, (agent_id,))
    agent = cur.fetchone()
    return agent

#Update agent
@app.put("/agents/{agent_id}")
def update_agent(agent_id: uuid, agent: Agent):
    query = "UPDATE agent SET updated_at = %s, first_name = %s, last_name = %s, email = %s, employee_num = %s WHERE id = %s"
    cur.execute(query, (agent.updated_at, agent.first_name, agent.last_name, agent.email, agent.employee_num, agent_id))
    conn.commit()
    return {"message": "Agent updated successfully"}

#Delete agent
@app.delete("/agents/{agent_id}")
def delete_agent(agent_id: uuid):
    query = "DELETE FROM agent WHERE id = %s"
    cur.execute(query, (agent_id,))
    conn.commit()
    return {"message": "Agent deleted successfully"}
