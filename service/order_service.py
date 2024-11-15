from model.Order import Order
from repository.order_repository import order_repository
from service.stock_service import subtraction_stock, get_stock_by_name


def create_order(order: Order) -> Order:
    return order_repository.create_order(order)


def get_order_by_id(order_id: int) -> Order:
    return order_repository.get_order_by_id(order_id)


def process_order(order: Order) -> Order:
    # Start processing the order rounds
    for currentRound in order.rounds:
        # Take each item from the current round
        for currentItem in currentRound.items:
            # Check if the stock is available
            stock = get_stock_by_name(currentItem.name)
            # If the stock is available and the quantity is enough, subtract the stock
            if stock is not None and stock.quantity >= currentItem.quantity:
                # Subtract the stock
                subtraction_stock(stock)
            else:
                # If the stock is not available or the quantity is not enough, set the order status to FAILED
                order.status = "FAILED"
                order.details = "Out of stock"
                # Update the order
                order_repository.update_order(order)
                return order
    return order


def update_order(order_id: int, order: Order) -> Order:
    order_repository.update_order(order)
    return order
