from pydantic import BaseModel


class Item(BaseModel):
    id: int
    name: str
    price_per_unit: int
    total: int
