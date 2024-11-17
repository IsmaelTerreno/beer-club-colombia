import copy

from model.Order import Order, StatusOrder
from repository.order_repository import order_repository
from service.stock_service import subtraction_stock, get_stock_by_id


def create_order(order: Order) -> Order:
    return order_repository.create_order(order)


def get_order_by_id(order_id: int) -> Order:
    return order_repository.get_order_by_id(order_id)


def process_order(order: Order) -> Order:
    is_all_rounds_processed = True
    order_in_process = copy.deepcopy(order)
    # Start processing the order rounds
    for currentRound in order_in_process.rounds:
        # Take each item from the current round
        for currentItem in currentRound.selected_items:
            # Check if the stock is available
            stock = get_stock_by_id(currentItem.id_item)
            # If the stock is available and the quantity is enough, subtract the stock
            if stock is not None and stock.quantity >= currentItem.quantity:
                # Subtract the stock
                is_taken = subtraction_stock(currentItem.id_item, currentItem.quantity)
                if is_taken:
                    # Add the processed item to the order
                    order_in_process.processed_items.append(currentItem)
                else:
                    is_all_rounds_processed = False
            else:
                is_all_rounds_processed = False
    if is_all_rounds_processed:
        order_in_process.paid = True
        order_in_process.status = StatusOrder.COMPLETED
        # Update the order
        order_repository.update_order(order_in_process)
    else:
        order_in_process.status = StatusOrder.FAILED
        # Update the order
        order_repository.update_order(order_in_process)
    # Return the updated order already processed
    updated_order = order_repository.get_order_by_id(order.id)
    return updated_order


def update_order(order_id: int, order: Order) -> Order:
    order_repository.update_order(order)
    return order


def delete_order(order_id: int) -> bool:
    order_repository.delete_order(order_id)
    return True
