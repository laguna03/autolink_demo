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
class Sale(BaseModel):
    id: int
    service_id: int
    agent_id: uuid
    status: str
    updated_at: datetime
    final_price: float

#CRUD operations for sale table

#Create sale
@app.post("/sales/")
def create_sale(sale: Sale):
    query = "INSERT INTO sale (id, service_id, agent_id, status, updated_at, final_price) VALUES (%s, %s, %s, %s, %s, %s)"
    cur.execute(query, (sale.id, sale.service_id, sale.agent_id, sale.status, sale.updated_at, sale.final_price))
    conn.commit()
    return {"message": "Invoice created successfully"}

#Read sale
@app.get("/sales/{sale_id}")
def read_sale(sale_id: int):
    query = "SELECT * FROM sale WHERE id = %s"
    cur.execute(query, (sale_id,))
    sale = cur.fetchone()
    return sale

#Update sale
@app.put("/sales/{sale_id}")
def update_sale(sale_id: int, sale: Sale):
    query = "UPDATE sale SET service_id = %s, agent_id = %s, status = %s, updated_at = %s, final_price = %s WHERE id = %s"
    cur.execute(query, (sale.service_id, sale.agent_id, sale.status, sale.updated_at, sale.final_price, sale_id))
    conn.commit()
    return {"message": "Invoice updated successfully"}

#Delete sale
@app.delete("/sales/{sale_id}")
def delete_sale(sale_id: int):
    query = "DELETE FROM sale WHERE id = %s"
    cur.execute(query, (sale_id,))
    conn.commit()
    return {"message": "Invoice deleted successfully"}
