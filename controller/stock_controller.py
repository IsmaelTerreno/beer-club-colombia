from starlette.responses import JSONResponse

from main import app
from model.Order import Order


@app.post("/api/v1/order")
async def create_order(order: Order):
    return JSONResponse(content={"message": "Order created successfully", "data": order.dict()}, status_code=201)
