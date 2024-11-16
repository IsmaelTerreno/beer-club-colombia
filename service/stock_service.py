from model.Stock import Stock
from repository.stock_repository import stock_repository


def subtraction_stock(beer_id: int, quantity: int) -> bool:
    stock = stock_repository.get_stock_by_id(beer_id)
    if stock is not None and stock.quantity >= quantity:
        stock.quantity -= quantity
        return True
    return False


def addition_stock(beer_id: int, quantity: int) -> bool:
    stock = stock_repository.get_stock_by_id(beer_id)
    if stock is not None:
        stock.quantity += quantity
        return True
    return False


def get_stock_by_id(stock_id: int) -> Stock:
    return stock_repository.get_stock_by_id(stock_id)
