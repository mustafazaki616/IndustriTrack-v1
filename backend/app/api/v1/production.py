from fastapi import APIRouter

router = APIRouter()

@router.get("/orders")
async def get_work_orders():
    return {"orders": []}

@router.post("/bom")
async def create_bom():
    return {"message": "BOM created"}
