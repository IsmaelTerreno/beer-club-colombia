from model.Stock import Stock
from repository.stock_repository import stock_inventory_in_memory_store
from repository.stock_repository import stock_repository


def subtraction_stock(stock: Stock) -> Stock:
    for beer in stock_inventory_in_memory_store.beers:
        stock_beer = stock_repository.get_stock_by_id(beer.id)
        if stock_beer is not None:
            stock_beer.quantity -= beer.quantity
    return stock


def addition_stock(stock: Stock) -> Stock:
    for beer in stock_inventory_in_memory_store.beers:
        stock_beer = stock_repository.get_stock_by_id(beer.id)
        if stock_beer is not None:
            stock_beer.quantity += beer.quantity
    return stock


def get_stock_by_id(stock_id: int) -> Stock:
    return stock_repository.get_stock_by_id(stock_id)
