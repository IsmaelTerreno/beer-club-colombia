from model.Stock import Stock
from repository.stock_repository import stock_repository


def subtraction_stock(beer_id: str, quantity: int) -> bool:
    """
    This function decreases the stock quantity based on the given beer ID and quantity.

    :param beer_id: The ID of the beer whose stock is to be decreased.
    :type beer_id: str

    :param quantity: The amount to decrease from the stock.
    :type quantity: int

    :return: True if the stock was successfully decreased, False otherwise.
    :rtype: bool
    """
    stock = stock_repository.get_beer_by_id(beer_id)
    if stock is not None and stock.quantity >= quantity:
        stock.quantity -= quantity
        return True
    return False


def addition_stock(beer_id: int, quantity: int) -> bool:
    """
    The addition_stock function adds a specified quantity of beer to the existing stock.

    :param beer_id: The unique identifier of the beer.
    :type beer_id: int
    :param quantity: The amount of beer to add to the stock.
    :type quantity: int
    :return: Whether the stock was successfully updated.
    :rtype: bool
    """
    stock = stock_repository.get_beer_by_id(beer_id)
    if stock is not None:
        stock.quantity += quantity
        return True
    return False


def get_stock_by_id(stock_id: str) -> Stock:
    """
    Fetches a stock object from the repository using its unique identifier.

    :param stock_id: The unique identifier of the stock to be retrieved.
    :type stock_id: str
    :return: The stock object corresponding to the given stock_id.
    :rtype: Stock
    """
    return stock_repository.get_beer_by_id(stock_id)


def get_stock() -> Stock:
    """
    Retrieve a stock object from the stock repository.

    This function calls the stock repository to fetch and return a Stock
    object containing the current stock details.

    :return: A Stock object with the current stock information.
    :rtype: Stock
    """
    return stock_repository.get_stock()
