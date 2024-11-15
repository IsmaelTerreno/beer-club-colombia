from repository.data import inventory_in_memory_store


class StockRepository:
    def __init__(self):
        self.inventory = inventory_in_memory_store

    def get_stock(self):
        return self.inventory

    def save_stock(self, stock):
        self.inventory = stock

    def get_stock_by_name(self, name):
        return next((beer for beer in self.inventory.beers if beer.name == name), None)


# Initialize a single instance of StockRepository
stock_repository = StockRepository()
