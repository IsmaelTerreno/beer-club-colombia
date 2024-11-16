# test_order_endpoint_e2e.py

import pytest
from httpx import AsyncClient

from main import app


@pytest.mark.asyncio
async def test_should_create_order():
    async with AsyncClient(app=app, base_url="http://localhost:8000") as ac:
        # Define the order payload
        order_payload = generate_order_payload(1)

        response = await ac.post("/api/v1/order", json=order_payload)

        assert response.status_code == 201
        assert response.json() == {
            "message": "Order created successfully",
            "data": order_payload,  # This should match the data format returned by `order.dict()`
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
            "data": order_payload,  # This should match the data format returned by `order.dict()`
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
            "data": order_payload,  # This should match the data format returned by `order.dict()`
        }

        # Find the order
        response = await ac.get("/api/v1/order/{}".format(id_to_test))
        assert response.status_code == 200
        assert response.json() == {
            "message": "Order not found",
            "data": None,
        }


def generate_order_payload(order_id: int):
    return {
        "id": order_id,
        "created": "2023-10-05T15:26:48.123456",
        "paid": False,
        "subtotal": 100.0,
        "taxes": 20.0,
        "discounts": 5.0,
        "items": [
            {
                "id": 1,
                "name": "Item 1",
                "price_per_unit": 25,
                "total": 50,
            },
            {
                "id": 2,
                "name": "Item 2",
                "price_per_unit": 25,
                "total": 50,
            },
        ],
        "rounds": [
            {
                "id": 1,
                "created": "2023-10-05T15:26:48.123456",
                "items": [
                    {"id": 1, "name": "Item 1", "price_per_unit": 25, "total": 50},
                    {"id": 2, "name": "Item 2", "price_per_unit": 25, "total": 50},
                ],
            }
        ],
        "status": "pending",
        "details": "This is a test order.",
    }