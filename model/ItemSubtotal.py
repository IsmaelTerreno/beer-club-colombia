from pydantic import BaseModel


class ItemSubtotal(BaseModel):
    """
    Represents the subtotal for an item in an order.

    This class encapsulates the details of an item subtotal, including the item ID,
    quantity, price per unit, and the calculated subtotal.

    :ivar id: Unique identifier for the item subtotal.
    :type id: str
    :ivar id_item: Unique identifier for the item.
    :type id_item: int
    :ivar quantity: Quantity of the item.
    :type quantity: int
    :ivar price_per_unit: Price per unit of the item.
    :type price_per_unit: int
    :ivar sub_total: Calculated subtotal for the item (quantity * price per unit).
    :type sub_total: int
    """
    id: str
    id_item: str
    quantity: int
    price_per_unit: int
    sub_total: int
