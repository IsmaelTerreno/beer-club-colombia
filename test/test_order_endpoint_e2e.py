# test_order_endpoint_e2e.py

import pytest
from httpx import AsyncClient

from main import app
from model.Order import StatusOrder


@pytest.mark.asyncio
async def test_should_create_order():
    async with AsyncClient(app=app, base_url="http://localhost:8000") as ac:
        # Define the order payload
        order_payload = generate_order_payload(1)
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
        id_to_test = 2
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
        id_to_test = 3
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
async def test_should_create_and_process_order():
    async with AsyncClient(app=app, base_url="http://localhost:8000") as ac:
        # Define the order payload id
        id_to_test = 4
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


def generate_order_payload(order_id: int):
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
                "id_item": 1,
                "name": "Corona",
            },
            {
                "id_item": 2,
                "name": "Quilmes",
            },
        ],
        "rounds": [
            {
                "id": 1,
                "created": "2023-10-05T15:26:48.123456",
                "selected_items": [
                    {
                        "id": 1,
                        "id_item": 1,
                        "quantity": 3,
                        "price_per_unit": 0,
                        "sub_total": 0,
                    },
                    {
                        "id": 2,
                        "id_item": 2,
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
