from model.Order import Order
from repository.order_repository import order_repository
from service.stock_service import subtraction_stock


def create_order(order: Order) -> Order:
    return order_repository.create_order(order)


def get_order_by_id(order_id: int) -> Order:
    return order_repository.get_order_by_id(order_id)


def process_order(order: Order) -> Order:
    order_repository.update_order(order)
    subtraction_stock(order)
    return order
