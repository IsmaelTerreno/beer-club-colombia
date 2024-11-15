from pydantic import BaseModel


class Beer(BaseModel):
    id: int
    name: str
    price: int
    quantity: int
