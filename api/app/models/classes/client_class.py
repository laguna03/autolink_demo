from datetime import date, datetime
from pydantic import BaseModel
from uuid import UUID


class ClientData(BaseModel):
    client_id: UUID
    updated_at: datetime
    first_name: str
    last_name: str
    email: str
    phone: str
    date_of_birth: date

class ClientResponse(BaseModel):
    first_name: str
    last_name: str
    email: str
    phone: str
    date_of_birth: date
