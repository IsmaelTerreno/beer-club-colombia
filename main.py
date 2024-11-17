from fastapi import FastAPI

from model.Order import Order, StatusOrder
from service.order_service import create_order, update_order, get_order_by_id, delete_order, process_order

app = FastAPI()


@app.get("/", summary="Root endpoint for welcome message")
async def root():
    return {"message": "Beer Club Colombia API. Welcome to the club!. You can access the API documentation at /docs"}


@app.post("/api/v1/order", status_code=201, summary="Create a new order")
async def create_order_endpoint(order: Order):
    """
    Create a new order.

    This endpoint allows for the creation of a new order by accepting order
    details in the request body and returning a confirmation message along with the
    created order data.

    :param order: Order details to be created
    :type order: Order
    :return: Confirmation message and the created order data
    :rtype: dict
    """
    order = create_order(order)
    return {"message": "Order created successfully", "data": order}


@app.put("/api/v1/order/{order_id}", status_code=204, summary="Update an existing order")
async def update_order_endpoint(order_id: int, order: Order):
    """
    Update an existing order with given order details.

    :param order_id: The ID of the order to update
    :param order: The new order data to update with
    :return: A dictionary containing a success message and the updated order data
    """
    updated_order = update_order(order_id, order)
    return {"message": "Order updated successfully", "data": updated_order}


@app.get("/api/v1/order/{order_id}", status_code=200, summary="Find an existing order")
async def find_order_endpoint(order_id: int):
    """
    Find an existing order by its unique identifier.

    This endpoint retrieves the details of an order based on the provided order ID.
    If the order is found, it returns the order details; otherwise, it returns a
    message indicating that the order was not found.

    :param order_id: The unique identifier of the order to be retrieved.
    :type order_id: int

    :return: A dictionary containing a message and the order data, if available.
    :rtype: dict
    """
    order = get_order_by_id(order_id)
    if order is None:
        return {"message": "Order not found", "data": None}
    return {"message": "Order found", "data": order}


@app.delete("/api/v1/order/{order_id}", status_code=202, summary="Delete an existing order")
async def delete_order_endpoint(order_id: int):
    """
    Delete an existing order.

    This endpoint deletes an existing order given its unique identifier. It
    checks if the order exists and, if so, deletes it and returns a success
    message along with the deleted order data. If the order does not exist,
    it returns a message stating that the order was not found. If the deletion
    process fails, it returns a failure message along with the order data.

    :param order_id: The unique identifier of the order to be deleted
    :type order_id: int
    :return: A message indicating success or failure, with the relevant order data
    :rtype: dict
    """
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
    """
    Process an order

    This endpoint processes an incoming order based on the provided details.
    It updates the order status and returns an appropriate message along with
    the processed order data.

    :param order: The order to be processed
    :type order: Order
    :return: A dictionary containing a message and the processed order data
    :rtype: dict
    """
    order = process_order(order)
    if order.status == StatusOrder.FAILED:
        return {"message": "Order processing failed", "data": order}
    return {"message": "Order processed successfully", "data": order}
