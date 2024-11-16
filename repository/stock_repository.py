from repository.data_in_memory import stock_inventory_in_memory_store


class StockRepository:
    def __init__(self):
        self.inventory = stock_inventory_in_memory_store

    def get_stock(self):
        return self.inventory

    def save_stock(self, stock):
        self.inventory = stock

    def get_stock_by_id(self, id_item):
        return next((beer for beer in self.inventory.beers if beer.id == id_item), None)


# Initialize a single instance of StockRepository
stock_repository = StockRepository()
