from fastapi import APIRouter

from service.stock_service import get_stock

router = APIRouter()


@router.get("/api/v1/stock/current", status_code=200, summary="Get current stock")
async def current_stock_endpoint():
    stock = get_stock()
    if stock is None:
        return {"message": "Stock not found", "data": None}
    return {"message": "Stock found", "data": stock}
