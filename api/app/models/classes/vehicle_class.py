from pydantic import BaseModel
from uuid import UUID


class VehicleData(BaseModel):
    id: int
    client_id: UUID
    license_plate: str
    vin_number: str
    make: str
    milage: int
    model: str
    year: int