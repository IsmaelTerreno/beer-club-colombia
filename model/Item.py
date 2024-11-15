from pydantic import BaseModel


class Item(BaseModel):
    name: str
    price_per_unit: int
    total: int
