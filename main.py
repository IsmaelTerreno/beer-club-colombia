from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from controller.order_controller import router as order_router
from controller.stock_controller import router as stock_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(order_router)
app.include_router(stock_router)


@app.get("/", summary="Root endpoint for welcome message")
async def root():
    return {"message": "Beer Club Colombia API. Welcome to the club!. You can access the API documentation at /docs"}
