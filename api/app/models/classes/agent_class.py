from pydantic import BaseModel
from datetime import datetime
from uuid import UUID

class AgentData(BaseModel):
    id: UUID
    updated_at: datetime
    first_name: str
    last_name: str
    email: str
    employee_num: str