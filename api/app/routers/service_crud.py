from fastapi import FastAPI
from pydantic import BaseModel
import psycopg2

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
class Service(BaseModel):
    id: int
    service_name: str
    service_description: str
    service_duration: int
    service_price: float

#CRUD operations for service table

#Create service
@app.post("/services/")
def create_service(service: Service):
    query = "INSERT INTO service (id, service_name, service_description, service_duration, service_price) VALUES (%s, %s, %s, %s, %s)"
    cur.execute(query, (service.id, service.service_name, service.service_description, service.service_duration, service.service_price))
    conn.commit()
    return {"message": "Work order created successfully"}

#Read service
@app.get("/services/{service_id}")
def read_service(service_id: int):
    query = "SELECT * FROM service WHERE id = %s"
    cur.execute(query, (service_id,))
    service = cur.fetchone()
    return service

#Update service
@app.put("/services/{service_id}")
def update_service(service_id: int, service: Service):
    query = "UPDATE service SET service_name = %s, service_description = %s, service_duration = %s, service_price = %s WHERE id = %s"
    cur.execute(query, (service.service_name, service.service_description, service.service_duration, service.service_price, service_id))
    conn.commit()
    return {"message": "Work order updated successfully"}

#Delete service
@app.delete("/services/{service_id}")
def delete_service(service_id: int):
    query = "DELETE FROM service WHERE id = %s"
    cur.execute(query, (service_id,))
    conn.commit()
    return {"message": "Work order deleted successfully"}
