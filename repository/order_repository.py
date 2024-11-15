from repository.data_in_memory import orders_in_memory_store


class OrderRepository:
    def create_order(self, order):
        orders_in_memory_store.append(order)
        return order


order_repository = OrderRepository()
