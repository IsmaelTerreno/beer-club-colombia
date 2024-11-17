import copy

from model.ItemSubtotal import ItemSubtotal
from model.ItemsRequestRound import ItemsRequestRound
from model.Order import Order, StatusOrder
from repository.order_repository import order_repository
from service.stock_service import subtraction_stock, get_stock_by_id


def create_order(order: Order) -> Order:
    return order_repository.create_order(order)


def get_order_by_id(order_id: int) -> Order:
    return order_repository.get_order_by_id(order_id)


def process_order(order: Order) -> Order:
    is_all_rounds_processed_by_stock = True
    order_in_progress = copy.deepcopy(order)
    result_details = ""
    # Start processing the order rounds
    for currentRound in order_in_progress.rounds:
        # Take each item from the current round
        for currentItem in currentRound.selected_items:
            # Check if the stock is available
            stock = get_stock_by_id(currentItem.id_item)
            # If the stock is available and the quantity is enough, subtract the stock
            if stock is not None and stock.quantity >= currentItem.quantity:
                # Subtract the stock
                is_taken = subtraction_stock(currentItem.id_item, currentItem.quantity)
                if is_taken:
                    # Set the price per unit of the item
                    currentItem.price_per_unit = stock.price_per_unit
                    # Calculate the subtotal of each processed item
                    currentItem.sub_total = currentItem.quantity * currentItem.price_per_unit
                    # Add the processed item to the order
                    order_in_progress.processed_items.append(currentItem)
                else:
                    # If the stock is not taken for any item in the list, set the order status to FAILED
                    is_all_rounds_processed_by_stock = False
                    result_details = get_error_message_item(currentItem, currentRound)
            else:
                # If the stock is not available, set the order status to FAILED
                is_all_rounds_processed_by_stock = False
                result_details = get_error_message_item(currentItem, currentRound)
    if is_all_rounds_processed_by_stock:
        # Calculate the total to pay from processed items including taxes and discounts
        order_in_progress.total_to_pay = (sum([item.sub_total for item in
                                               order_in_progress.processed_items]) + order_in_progress.taxes) - order_in_progress.discounts
        # Calculate the cash returned to the customer
        order_in_progress.cash_returned = order_in_progress.cash_tendered - order_in_progress.total_to_pay
        # Set the order as paid if the cash tendered is greater than the total to pay
        is_paid = order_in_progress.cash_tendered >= order_in_progress.total_to_pay
        # Set the order paid status
        order_in_progress.paid = is_paid
        # If all the rounds are processed and the order is paid, set the order status to COMPLETED
        order_in_progress.status = StatusOrder.COMPLETED if is_paid else StatusOrder.FAILED
        # If all the rounds are processed and the order is paid set the details message
        result_details = "Order processed successfully" if is_paid else "Order failed to process due to insufficient cash"
    # Set the details message
    order_in_progress.details = result_details
    # Update the order in the repository in memory
    order_repository.update_order(order_in_progress)
    # Return the updated order already processed
    updated_order = order_repository.get_order_by_id(order.id)
    return updated_order


def get_error_message_item(current_item: ItemSubtotal, current_round: ItemsRequestRound):
    return "Order failed to process due to insufficient stock of item with id: " + str(
        current_item.id_item) + " in round with id: " + str(current_round.id)


def update_order(order_id: int, order: Order) -> Order:
    order_repository.update_order(order)
    return order


def delete_order(order_id: int) -> bool:
    order_repository.delete_order(order_id)
    return True
