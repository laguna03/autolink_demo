from app.models.sales_operations import create_sale, read_sale, update_sale, delete_sale, Sale
from fastapi import APIRouter
from uuid import UUID

router = APIRouter()

@router.post("/sales/")
async def create_sale_endpoint(sale_data: Sale) -> dict:
    create_sale(sale_data)
    return {"message": "Sale created successfully"}

@router.get("/sales/{sale_id}")
async def read_sale_endpoint(sale_id: int) -> Sale:
    return read_sale(sale_id)

@router.put("/sales/{sale_id}")
async def update_sale_endpoint(sale_id: int, sale_data: Sale) -> dict:
    update_sale(sale_id, sale_data)
    return {"message": "Sale updated successfully"}

@router.delete("/sales/{sale_id}")
async def delete_sale_endpoint(sale_id: int) -> dict:
    delete_sale(sale_id)
    return {"message": "Sale deleted successfully"}
