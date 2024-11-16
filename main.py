from fastapi import FastAPI

from model.Order import Order
from service.order_service import create_order, update_order

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/api/v1/order", status_code=201, summary="Create a new order")
async def create_order_endpoint(order: Order):
    order = create_order(order)
    return {"message": "Order created successfully", "data": order.dict()}


@app.put("/api/v1/order/{order_id}", status_code=200, summary="Update an existing order")
async def update_order_endpoint(order_id: int, order: Order):
    updated_order = update_order(order_id, order)
    return {"message": "Order updated successfully", "data": updated_order.dict()}
