from datetime import date, datetime
from pydantic import BaseModel
from uuid import UUID


class ClientData(BaseModel):
    id: UUID
    updated_at: datetime
    first_name: str
    last_name: str
    email: str
    phone: str
    date_of_birth: date