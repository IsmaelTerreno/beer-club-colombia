# test_order_endpoint_e2e.py
import uuid

import pytest
from httpx import AsyncClient

from main import app
from model.Order import StatusOrder


@pytest.mark.asyncio
async def test_should_create_order():
    async with AsyncClient(app=app, base_url="http://localhost:8000") as ac:
        # Define the order payload
        order_payload = generate_order_payload(str(uuid.uuid4()))
        # Create the order
        response = await ac.post("/api/v1/order", json=order_payload)
        # Assert the response with the expected values
        assert response.status_code == 201
        assert response.json() == {
            "message": "Order created successfully",
            "data": order_payload,
        }


@pytest.mark.asyncio
async def test_should_create_and_find_existing_order():
    async with AsyncClient(app=app, base_url="http://localhost:8000") as ac:
        # Define the order payload id
        id_to_test = str(uuid.uuid4())
        # Define the order payload
        order_payload = generate_order_payload(id_to_test)

        # Create the order
        response = await ac.post("/api/v1/order", json=order_payload)
        assert response.status_code == 201

        # Find the order
        response = await ac.get("/api/v1/order/{}".format(id_to_test))
        assert response.status_code == 200
        assert response.json() == {
            "message": "Order found",
            "data": order_payload,
        }


@pytest.mark.asyncio
async def test_should_create_and_delete_existing_order():
    async with AsyncClient(app=app, base_url="http://localhost:8000") as ac:
        # Define the order payload id
        id_to_test = str(uuid.uuid4())
        # Define the order payload
        order_payload = generate_order_payload(id_to_test)

        # Create the order
        response = await ac.post("/api/v1/order", json=order_payload)
        assert response.status_code == 201

        # Delete the order
        response = await ac.delete("/api/v1/order/{}".format(id_to_test))
        assert response.status_code == 202
        assert response.json() == {
            "message": "Order deleted",
            "data": order_payload,
        }

        # Find the order
        response = await ac.get("/api/v1/order/{}".format(id_to_test))
        assert response.status_code == 200
        assert response.json() == {
            "message": "Order not found",
            "data": None,
        }


@pytest.mark.asyncio
async def test_should_create_and_process_order_with_success():
    async with AsyncClient(app=app, base_url="http://localhost:8000") as ac:
        # Define the order payload id
        id_to_test = str(uuid.uuid4())
        # Define the order payload
        order_payload = generate_order_payload(id_to_test)

        # Create the order
        response = await ac.post("/api/v1/order", json=order_payload)
        assert response.status_code == 201

        # Process the order
        response = await ac.post("/api/v1/order/process", json=order_payload)
        assert response.status_code == 200
        # Check the status of the order completed
        assert response.json()["data"]["status"] == str(StatusOrder.COMPLETED.value)
        # Check the total to pay
        assert response.json()["data"]["total_to_pay"] == 480.0
        # Check the cash returned
        assert response.json()["data"]["cash_returned"] == 1520.0
        # Check the order paid status
        assert response.json()["data"]["paid"] is True
        # Check the details message
        assert response.json()["data"]["details"] == "Order processed successfully"


@pytest.mark.asyncio
async def test_should_create_and_process_order_with_failure_due_to_insufficient_funds():
    async with AsyncClient(app=app, base_url="http://localhost:8000") as ac:
        # Define the order payload id
        id_to_test = str(uuid.uuid4())
        # Define the order payload
        order_payload = generate_order_payload(id_to_test)
        # Set the cash tendered to 0.0
        order_payload["cash_tendered"] = 0.0

        # Create the order
        response = await ac.post("/api/v1/order", json=order_payload)
        assert response.status_code == 201

        # Process the order
        response = await ac.post("/api/v1/order/process", json=order_payload)
        assert response.status_code == 200
        # Check the status of the order failed
        assert response.json()["data"]["status"] == str(StatusOrder.FAILED.value)
        # Check the total to pay
        assert response.json()["data"]["total_to_pay"] == 480.0
        # Check the cash returned
        assert response.json()["data"]["cash_returned"] == 0.0
        # Check the order paid status
        assert response.json()["data"]["paid"] is False
        # Check the details message
        assert response.json()["data"]["details"] == "Order failed to process due to insufficient cash"


@pytest.mark.asyncio
async def test_should_create_and_process_order_with_failure_due_to_insufficient_stock_of_item():
    async with AsyncClient(app=app, base_url="http://localhost:8000") as ac:
        # Define the order payload id
        id_to_test = str(uuid.uuid4())
        # Define the order payload
        order_payload = generate_order_payload(id_to_test)
        # Set the quantity of the item to 10000
        order_payload["rounds"][0]["selected_items"][0]["quantity"] = 10000
        # Set the tendered cash to 2000.0
        order_payload["cash_tendered"] = 2000.0
        # Create the order
        response = await ac.post("/api/v1/order", json=order_payload)
        assert response.status_code == 201

        # Process the order
        response = await ac.post("/api/v1/order/process", json=order_payload)
        assert response.status_code == 200
        # Check the status of the order failed
        assert response.json()["data"]["status"] == str(StatusOrder.FAILED.value)
        # Check the total to pay
        assert response.json()["data"]["total_to_pay"] == 0.0
        # Check the cash returned
        assert response.json()["data"]["cash_returned"] == 2000.0
        # Check the order paid status
        assert response.json()["data"]["paid"] is False
        # Check the details message
        assert response.json()["data"][
                   "details"] == "Order failed to process due to insufficient stock of item with id: 1 in round with id: 1"


@pytest.mark.asyncio
async def test_should_get_current_stock():
    async with AsyncClient(app=app, base_url="http://localhost:8000") as ac:
        response = await ac.get("/api/v1/stock/current")
        assert response.status_code == 200
        # Check the message
        assert response.json()["message"] == "Stock found"
        # Check the data is not None
        assert response.json()["data"] is not None


def generate_order_payload(order_id: str):
    beer_corona_id = str(uuid.uuid4())
    beer_quilmes_id = str(uuid.uuid4())
    return {
        "id": order_id,
        "created": "2023-10-05T15:26:48.123456",
        "paid": False,
        "subtotal": 100.0,
        "taxes": 20.0,
        "discounts": 5.0,
        "total_to_pay": 0.0,
        "cash_tendered": 2000.0,
        "cash_returned": 0.0,
        "option_items": [
            {
                "id_item": beer_corona_id,
                "name": "Corona",
            },
            {
                "id_item": beer_quilmes_id,
                "name": "Quilmes",
            },
        ],
        "rounds": [
            {
                "id": str(uuid.uuid4()),
                "created": "2023-10-05T15:26:48.123456",
                "selected_items": [
                    {
                        "id": str(uuid.uuid4()),
                        "id_item": beer_corona_id,
                        "quantity": 3,
                        "price_per_unit": 0,
                        "sub_total": 0,
                    },
                    {
                        "id": str(uuid.uuid4()),
                        "id_item": beer_quilmes_id,
                        "quantity": 1,
                        "price_per_unit": 0,
                        "sub_total": 0,
                    },
                ],
            }
        ],
        "status": str(StatusOrder.PENDING),
        "details": "This is a test order.",
        "processed_items": []
    }
