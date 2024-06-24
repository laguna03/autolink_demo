from pydantic import BaseModel



class ServiceData(BaseModel):
    service_id: int
    service_name: str
    service_description: str
    service_duration: int
    service_price: float