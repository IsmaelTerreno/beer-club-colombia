from fastapi import FastAPI

from model.Order import Order, StatusOrder
from service.order_service import create_order, update_order, get_order_by_id, delete_order, process_order

app = FastAPI()


@app.get("/", summary="Root endpoint for welcome message")
async def root():
    return {"message": "Beer Club Colombia API. Welcome to the club!. You can access the API documentation at /docs"}


@app.post("/api/v1/order", status_code=201, summary="Create a new order")
async def create_order_endpoint(order: Order):
    order = create_order(order)
    return {"message": "Order created successfully", "data": order}


@app.put("/api/v1/order/{order_id}", status_code=204, summary="Update an existing order")
async def update_order_endpoint(order_id: int, order: Order):
    updated_order = update_order(order_id, order)
    return {"message": "Order updated successfully", "data": updated_order}


@app.get("/api/v1/order/{order_id}", status_code=200, summary="Find an existing order")
async def find_order_endpoint(order_id: int):
    order = get_order_by_id(order_id)
    if order is None:
        return {"message": "Order not found", "data": None}
    return {"message": "Order found", "data": order}


@app.delete("/api/v1/order/{order_id}", status_code=202, summary="Delete an existing order")
async def delete_order_endpoint(order_id: int):
    order = get_order_by_id(order_id)
    if order is None:
        return {"message": "Order not found", "data": None}
    else:
        is_deleted = delete_order(order_id)
        if not is_deleted:
            return {"message": "Failed to delete order", "data": order}
        return {"message": "Order deleted", "data": order}


@app.post("/api/v1/order/process", status_code=200, summary="Process an order")
async def process_order_endpoint(order: Order):
    order = process_order(order)
    if order.status == StatusOrder.FAILED:
        return {"message": "Order processing failed", "data": order}
    return {"message": "Order processed successfully", "data": order}
