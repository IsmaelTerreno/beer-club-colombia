from fastapi import FastAPI

from controller.order_controller import router as order_router

app = FastAPI()

app.include_router(order_router)


@app.get("/", summary="Root endpoint for welcome message")
async def root():
    return {"message": "Beer Club Colombia API. Welcome to the club!. You can access the API documentation at /docs"}
