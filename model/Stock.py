from datetime import datetime
from typing import List

from pydantic import BaseModel

from model.Beer import Beer


class Stock(BaseModel):
    """
    Represents a stock and its associated details.

    This class holds information about a stock including its ID, the date
    and time it was last updated, and a list of beers associated with the
    stock.

    :ivar id: Unique identifier for the stock.
    :type id: str
    :ivar last_updated: Timestamp of the last update to the stock.
    :type last_updated: datetime
    :ivar beers: List of beers associated with the stock.
    :type beers: List[Beer]
    """
    id: str
    last_updated: datetime
    beers: List[Beer]
