from pydantic import BaseModel


class Beer(BaseModel):
    """
    Represents a beer with its attributes such as id, name, price, and quantity.

    This model is used for managing information about different types of beers,
    including their identification, name, cost, and available stock.

    :ivar id: The unique identifier for the beer.
    :type id: str
    :ivar name: The name of the beer.
    :type name: str
    :ivar price_per_unit: The price of the beer.
    :type price_per_unit: int
    :ivar quantity: The quantity of the beer in stock.
    :type quantity: int
    """
    id: str
    name: str
    price_per_unit: int
    quantity: int
