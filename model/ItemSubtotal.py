from pydantic import BaseModel


class ItemSubtotal(BaseModel):
    """
    Represents the subtotal for an item in an order.

    This class encapsulates the details of an item subtotal, including the item ID,
    quantity, price per unit, and the calculated subtotal.

    :ivar id: Unique identifier for the item subtotal.
    :type id: int
    :ivar id_item: Unique identifier for the item.
    :type id_item: int
    :ivar quantity: Quantity of the item.
    :type quantity: int
    :ivar price_per_unit: Price per unit of the item.
    :type price_per_unit: str
    :ivar sub_total: Calculated subtotal for the item (quantity * price per unit).
    :type sub_total: int
    """
    id: int
    id_item: int
    quantity: int
    price_per_unit: str
    sub_total: int
