from datetime import datetime
from enum import Enum
from typing import List

from pydantic import BaseModel

from model.Item import Item
from model.ItemSubtotal import ItemSubtotal
from model.ItemsRequestRound import ItemsRequestRound


class StatusOrder(Enum):
    """
    Represents the various statuses an order can have.

    This enumeration is used to define the possible states of an order,
    which can be FAILED, PENDING, or COMPLETED. It serves the purpose
    of providing a clear and standardized way to check and set the state
    of an order within the system.

    :ivar FAILED: Indicates that the order has failed.
    :type FAILED: str
    :ivar PENDING: Indicates that the order is pending.
    :type PENDING: str
    :ivar COMPLETED: Indicates that the order is completed.
    :type COMPLETED: str
    """
    FAILED = "FAILED"
    PENDING = "PENDING"
    COMPLETED = "COMPLETED"


class Order(BaseModel):
    """
    Represents a customer order.

    This class is used to hold all information related to a customer's order,
    including financial details, status, and processed items.

    :ivar id: Unique identifier for the order.
    :type id: str
    :ivar created: Date and time when the order was created.
    :type created: datetime
    :ivar paid: Indicates whether the order has been paid.
    :type paid: bool
    :ivar subtotal: Subtotal amount for the order before taxes, discounts, etc.
    :type subtotal: float
    :ivar taxes: Total tax amount applicable to the order.
    :type taxes: float
    :ivar discounts: Total amount of discounts applied to the order.
    :type discounts: float
    :ivar total_to_pay: Total amount to be paid by the customer.
    :type total_to_pay: float
    :ivar cash_tendered: Amount of cash provided by the customer.
    :type cash_tendered: float
    :ivar cash_returned: Amount of cash returned to the customer as change.
    :type cash_returned: float
    :ivar option_items: List of items selected as options.
    :type option_items: List[Item]
    :ivar rounds: List of item request rounds.
    :type rounds: List[ItemsRequestRound]
    :ivar status: Current status of the order.
    :type status: str
    :ivar details: Additional details or notes about the order.
    :type details: str
    :ivar processed_items: List of items that have been processed with subtotals.
    :type processed_items: List[ItemSubtotal]
    """
    id: str
    created: datetime
    paid: bool
    subtotal: float
    taxes: float
    discounts: float
    total_to_pay: float
    cash_tendered: float
    cash_returned: float
    option_items: List[Item]
    rounds: List[ItemsRequestRound]
    status: str
    details: str
    processed_items: List[ItemSubtotal]
