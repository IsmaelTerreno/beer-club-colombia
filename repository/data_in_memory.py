import datetime

from model.Beer import Beer
from model.Order import Order
from model.Stock import Stock

# Initial values to start the app for the first time with some stock inventory
stock_inventory_in_memory_store: Stock = Stock(
    id=1,
    last_updated=datetime.datetime.now(),
    beers=[
        Beer(
            id=1,
            name="Corona",
            price_per_unit=115,
            quantity=12
        ),
        Beer(
            id=2,
            name="Quilmes",
            price_per_unit=120,
            quantity=31
        ),
        Beer(
            id=3,
            name="Club Colombia",
            price_per_unit=110,
            quantity=35
        )
    ],
)
# Initial values to start the app for the first time with clean orders
orders_in_memory_store: [Order] = []
