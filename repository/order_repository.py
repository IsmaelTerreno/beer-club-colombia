from repository.data_in_memory import orders_in_memory_store


class OrderRepository:
    def create_order(self, order):
        orders_in_memory_store.append(order)
        return order

    def get_order_by_id(self, order_id):
        for order in orders_in_memory_store:
            if order.id == order_id:
                return order
        return None

    def update_order(self, order):
        for i in range(len(orders_in_memory_store)):
            if orders_in_memory_store[i].id == order.id:
                orders_in_memory_store[i] = order
                return order
        return None


order_repository = OrderRepository()
