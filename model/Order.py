from datetime import datetime
from enum import Enum
from typing import List

from pydantic import BaseModel

from model.Item import Item
from model.ItemSubtotal import ItemSubtotal
from model.ItemsRequestRound import ItemsRequestRound


class StatusOrder(Enum):
    FAILED = "FAILED"
    PENDING = "PENDING"
    COMPLETED = "COMPLETED"


class Order(BaseModel):
    """
    Represents an order in a sales system.

    Detailed description of the class, its purpose, and usage. This class models the
    essential attributes of an order including financial details, statuses, and item
    details required for processing a transaction.

    :ivar id: The unique identifier for the order.
    :type id: int
    :ivar created: The datetime when the order was created.
    :type created: datetime
    :ivar paid: Indicates if the order has been paid for.
    :type paid: bool
    :ivar subtotal: The subtotal amount before taxes and discounts.
    :type subtotal: float
    :ivar taxes: The amount of taxes applied to the order.
    :type taxes: float
    :ivar discounts: The amount of discounts applied to the order.
    :type discounts: float
    :ivar cash_tendered: The amount of cash received for the order.
    :type cash_tendered: float
    :ivar option_items: The list of items including their options in the order.
    :type option_items: List[Item]
    :ivar rounds: The list of rounds associated with the order.
    :type rounds: List[ItemsRequestRound]
    :ivar status: The current status of the order.
    :type status: str
    :ivar details: Additional details or notes pertaining to the order.
    :type details: str
    :ivar processed_items: The list of processed items and their subtotals in the order.
    :type processed_items: List[ItemSubtotal]
    """
    id: int
    created: datetime
    paid: bool
    subtotal: float
    taxes: float
    discounts: float
    cash_tendered: float
    option_items: List[Item]
    rounds: List[ItemsRequestRound]
    status: str
    details: str
    processed_items: List[ItemSubtotal]
