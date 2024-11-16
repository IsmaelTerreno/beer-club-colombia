from datetime import datetime
from enum import Enum
from typing import List

from pydantic import BaseModel

from model.Item import Item
from model.Round import Round


class StatusOrder(Enum):
    FAILED = "FAILED"
    PENDING = "PENDING"
    COMPLETED = "COMPLETED"


class Order(BaseModel):
    id: int
    created: datetime
    paid: bool
    subtotal: float
    taxes: float
    discounts: float
    items: List[Item]
    rounds: List[Round]
    status: str
    details: str
