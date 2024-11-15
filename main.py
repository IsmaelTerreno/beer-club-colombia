from fastapi import FastAPI
from fastapi.responses import JSONResponse

from model.Order import Order

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/api/v1/order")
async def create_order(order: Order):
    return JSONResponse(content={"message": "Order created successfully", "data": order.dict()}, status_code=201)
