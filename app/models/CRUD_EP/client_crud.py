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
class Client(BaseModel):
    id: uuid
    updated_at: datetime
    first_name: str
    last_name: str
    email: str
    phone: str
    date_of_birth: date

#CRUD operations for client table

#Create client
@app.post("/clients/")
def create_client(client: Client):
    query = "INSERT INTO client (id, updated_at, first_name, last_name, email, phone, date_of_birth) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    cur.execute(query, (client.id, client.updated_at, client.first_name, client.last_name, client.email, client.phone, client.date_of_birth))
    conn.commit()
    return {"message": "Client created successfully"}

#Read client
@app.get("/clients/{client_id}")
def read_client(client_id: uuid):
    query = "SELECT * FROM client WHERE id = %s"
    cur.execute(query, (client_id,))
    client = cur.fetchone()
    return client

#Update client
@app.put("/clients/{client_id}")
def update_client(client_id: uuid, client: Client):
    query = "UPDATE client SET updated_at = %s, first_name = %s, last_name = %s, email = %s, phone = %s, date_of_birth = %s WHERE id = %s"
    cur.execute(query, (client.updated_at, client.first_name, client.last_name, client.email, client.phone, client.date_of_birth, client_id))
    conn.commit()
    return {"message": "Client updated successfully"}

#Delete client
@app.delete("/clients/{client_id}")
def delete_client(client_id: uuid):
    query = "DELETE FROM client WHERE id = %s"
    cur.execute(query, (client_id,))
    conn.commit()
    return {"message": "Client deleted successfully"}

#Close cursor and connection
cur.close()
conn.close()
