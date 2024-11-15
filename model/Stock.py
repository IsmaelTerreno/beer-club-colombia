from datetime import datetime
from typing import List

from pydantic import BaseModel

from model.Beer import Beer


class Stock(BaseModel):
    id: int
    last_updated: datetime
    beers: List[Beer]
