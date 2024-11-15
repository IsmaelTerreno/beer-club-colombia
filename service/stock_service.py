from model.Stock import Stock
from repository.stock_repository import stock_repository


def subtraction_stock(stock: Stock, stock_to_subtract: Stock) -> Stock:
    for beer in stock_to_subtract.beers:
        stock_beer = stock_repository.get_stock_by_name(beer.name)
        if stock_beer is not None:
            stock_beer.quantity -= beer.quantity
    return stock
