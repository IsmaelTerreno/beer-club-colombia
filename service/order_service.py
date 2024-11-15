from model.Order import Order
from repository.order_repository import order_repository
from service.stock_service import subtraction_stock, get_stock_by_name


def create_order(order: Order) -> Order:
    return order_repository.create_order(order)


def get_order_by_id(order_id: int) -> Order:
    return order_repository.get_order_by_id(order_id)


def process_order(order: Order) -> Order:
    order_repository.update_order(order)
    for currentRound in order.rounds:
        for currentItem in currentRound.items:
            stock = get_stock_by_name(currentItem.name)
            if stock is not None and stock.quantity >= currentItem.quantity:
                subtraction_stock(stock)
            else:
                order.status = "FAILED"
                order.details = "Out of stock"
                order_repository.update_order(order)
                return order
    return order


def update_order(order_id: int, order: Order) -> Order:
    order_repository.update_order(order)
    return order
