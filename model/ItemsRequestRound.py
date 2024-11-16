from datetime import datetime
from typing import List

from pydantic import BaseModel

from model.Item import Item


class ItemsRequestRound(BaseModel):
    """
    Represents a request round for items.

    This class models a single request round for items, including details such as
    the unique identifier for the request, the creation timestamp, and a list of
    selected items associated with this request.

    :ivar id: Unique identifier for the request round.
    :type id: int
    :ivar created: Creation timestamp of the request round.
    :type created: datetime
    :ivar selected_items: List of items selected in this request round.
    :type selected_items: List[Item]
    """
    id: int
    created: datetime
    selected_items: List[Item]
