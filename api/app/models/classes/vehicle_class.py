from pydantic import BaseModel
from uuid import UUID


class VehicleData(BaseModel):
    vehicle_id: int
    client_id: UUID
    license_plate: str
    vin_number: str
    make: str
    mileage: int
    model: str
    year: int
