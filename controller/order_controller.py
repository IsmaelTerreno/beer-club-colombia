from starlette.responses import JSONResponse

from main import app
from model.Order import Order
from service.order_service import create_order
from service.order_service import update_order


@app.post("/api/v1/order")
async def create_order_endpoint(order: Order):
    order = create_order(order)
    return JSONResponse(content={"message": "Order created successfully", "data": order.dict()}, status_code=201)


@app.put("/api/v1/order/{order_id}")
async def update_order_endpoint(order_id: int, order: Order):
    updated_order = update_order(order_id, order)
    return JSONResponse(content={"message": "Order updated successfully", "data": updated_order.dict()},
                        status_code=200)
