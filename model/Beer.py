from pydantic import BaseModel

class Beer(BaseModel):
    name: str
    price: int
    quantity: int