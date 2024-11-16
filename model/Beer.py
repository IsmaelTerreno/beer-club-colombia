from pydantic import BaseModel


class Beer(BaseModel):
    """
    Represents a beer with its attributes such as id, name, price, and quantity.

    This model is used for managing information about different types of beers,
    including their identification, name, cost, and available stock.

    :ivar id: The unique identifier for the beer.
    :type id: int
    :ivar name: The name of the beer.
    :type name: str
    :ivar price: The price of the beer.
    :type price: int
    :ivar quantity: The quantity of the beer in stock.
    :type quantity: int
    """
    id: int
    name: str
    price: int
    quantity: int
