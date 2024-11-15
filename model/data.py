import datetime

from model.Beer import Beer
from model.Stock import Stock

# Initial values to start the app
inventory_in_memory_store = Stock(
    last_updated=datetime.datetime.now(),
    beers=[
        Beer(
            name="Corona",
            price=115,
            quantity=2
        ),
        Beer(
            name="Quilmes",
            price=120,
            quantity=0
        ),
        Beer(
            name="Club Colombia",
            price=110,
            quantity=3
        )
    ],
)
