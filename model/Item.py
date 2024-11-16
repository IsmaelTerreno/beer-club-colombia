from pydantic import BaseModel


class Item(BaseModel):
    """
    Represents an item with an identifier and a name.

    Detailed description of the class, its purpose, and usage.

    :ivar id_item: Unique identifier for the item.
    :ivar name: Name of the item.
    """
    id_item: int
    name: str
