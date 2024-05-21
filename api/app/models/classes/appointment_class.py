from pydantic import BaseModel
from datetime import datetime, date
from uuid import UUID


class AppointmentData(BaseModel):
    id: int
    agent_id: UUID
    sale_id: int
    client_id: UUID
    service_id: int
    vehicle_id: int
    created_at: datetime
    status: str
    appt_time: date
