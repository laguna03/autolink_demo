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
class Appointment(BaseModel):
    id: int
    agent_id: uuid
    sale_id: int
    client_id: uuid
    service_id: int
    vehicule_id: int
    created_at: datetime
    status: str
    appt_time: date

#CRUD operations for appointment table

#Create appointment
@app.post("/appointments/")
def create_appointment(appointment: Appointment):
    query = "INSERT INTO appointment (id, agent_id, sale_id, client_id, service_id, vehicule_id, created_at, status, appt_time) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    cur.execute(query, (appointment.id, appointment.agent_id, appointment.sale_id, appointment.client_id, appointment.service_id, appointment.vehicule_id, appointment.created_at, appointment.status, appointment.appt_time))
    conn.commit()
    return {"message": "Appointment created successfully"}

#Read appointment
@app.get("/appointments/{appointment_id}")
def read_appointment(appointment_id: int):
    query = "SELECT * FROM appointment WHERE id = %s"
    cur.execute(query, (appointment_id,))
    appointment = cur.fetchone()
    return appointment

#Update appointment
@app.put("/appointments/{appointment_id}")
def update_appointment(appointment_id: int, appointment: Appointment):
    query = "UPDATE appointment SET agent_id = %s, sale_id = %s, client_id = %s, service_id = %s, vehicule_id = %s, created_at = %s, status = %s, appt_time = %s WHERE id = %s"
    cur.execute(query, (appointment.agent_id, appointment.sale_id, appointment.client_id, appointment.service_id, appointment.vehicule_id, appointment.created_at, appointment.status, appointment.appt_time, appointment_id))
    conn.commit()
    return {"message": "Appointment updated successfully"}

#Delete appointment
@app.delete("/appointments/{appointment_id}")
def delete_appointment(appointment_id: int):
    query = "DELETE FROM appointment WHERE id = %s"
    cur.execute(query, (appointment_id,))
    conn.commit()
    return {"message": "Appointment deleted successfully"}
