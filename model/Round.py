from datetime import datetime
from typing import List

from pydantic import BaseModel

from model.Item import Item


class Round(BaseModel):
    id: int
    created: datetime
    items: List[Item]
