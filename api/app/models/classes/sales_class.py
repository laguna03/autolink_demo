from pydantic import BaseModel
from datetime import datetime
from uuid import UUID


class Sale(BaseModel):
    id: int
    service_id: int
    agent_id: UUID
    status: str
    updated_at: datetime
    final_price: float