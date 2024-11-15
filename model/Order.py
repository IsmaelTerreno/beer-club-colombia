from datetime import datetime
from typing import List

from pydantic import BaseModel

from model.Item import Item
from model.Round import Round


class Order(BaseModel):
    created: datetime
    paid: bool
    subtotal: float
    taxes: float
    discounts: float
    items: List[Item]
    rounds: List[Round]
