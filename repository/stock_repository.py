from repository.data_in_memory import stock_inventory_in_memory_store


class StockRepository:
    """
    Manages the inventory of stock items in memory.

    This class provides methods to interact with an in-memory store of stock inventory,
    allowing for retrieval, saving, and fetching of stock items based on their ID.

    :ivar inventory: The in-memory store of the current stock inventory.
    :type inventory: StockInventory
    """

    def __init__(self):
        self.inventory = stock_inventory_in_memory_store

    def get_stock(self):
        return self.inventory

    def save_stock(self, stock):
        self.inventory = stock

    def get_beer_by_id(self, id_item):
        return next((beer for beer in self.inventory.beers if beer.id == id_item), None)


# Initialize a single instance of StockRepository
stock_repository = StockRepository()
