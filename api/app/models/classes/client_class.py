from datetime import date, datetime
from pydantic import BaseModel
from uuid import UUID


class ClientData(BaseModel):
    client_id: UUID
    first_name: str
    last_name: str
    email: str
    phone: str

class ClientResponse(BaseModel):
    first_name: str
    last_name: str
    email: str
    phone: str

