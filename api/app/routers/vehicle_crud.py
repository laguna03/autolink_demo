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
class Vehicle(BaseModel):
    id: int
    client_id: uuid
    license_plate: str
    vin_number: str
    make: str
    milage: int
    model: str
    year: int

#CRUD operations for vehicle table

#Create vehicle
@app.post("/vehicles/")
def create_vehicle(vehicle: Vehicle):
    query = "INSERT INTO vehicle (id, client_id, license_plate, vin_number, make, milage, model, year) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    cur.execute(query, (vehicle.id, vehicle.client_id, vehicle.license_plate, vehicle.vin_number, vehicle.make, vehicle.milage, vehicle.model, vehicle.year))
    conn.commit()
    return {"message": "Vehicle created successfully"}

#Read vehicle
@app.get("/vehicles/{vehicle_id}")
def read_vehicle(vehicle_id: int):
    query = "SELECT * FROM vehicle WHERE id = %s"
    cur.execute(query, (vehicle_id,))
    vehicle = cur.fetchone()
    return vehicle

#Update vehicle
@app.put("/vehicles/{vehicle_id}")
def update_vehicle(vehicle_id: int, vehicle: Vehicle):
    query = "UPDATE vehicle SET client_id = %s, license_plate = %s, vin_number = %s, make = %s, milage = %s, model = %s, year = %s WHERE id = %s"
    cur.execute(query, (vehicle.client_id, vehicle.license_plate, vehicle.vin_number, vehicle.make, vehicle.milage, vehicle.model, vehicle.year, vehicle_id))
    conn.commit()
    return {"message": "Vehicle updated successfully"}

#Delete vehicle
@app.delete("/vehicles/{vehicle_id}")
def delete_vehicle(vehicle_id: int):
    query = "DELETE FROM vehicle WHERE id = %s"
    cur.execute(query, (vehicle_id,))
    conn.commit()
    return {"message": "Vehicle deleted successfully"}
