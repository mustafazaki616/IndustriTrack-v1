from fastapi import APIRouter

router = APIRouter()

@router.get("/customers")
async def get_customers():
    return {"customers": []}

@router.post("/orders")
async def create_sales_order():
    return {"message": "Sales order created"}
