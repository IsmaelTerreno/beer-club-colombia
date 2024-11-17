import copy

from model.ItemSubtotal import ItemSubtotal
from model.ItemsRequestRound import ItemsRequestRound
from model.Order import Order, StatusOrder
from repository.order_repository import order_repository
from service.stock_service import subtraction_stock, get_stock_by_id


def create_order(order: Order) -> Order:
    """
    Creates a new order using the provided order details.

    This function takes an Order object as input, processes it, and stores it using
    the order repository. The created order is then returned.

    :param order: Order object containing the details of the order to be created
    :type order: Order
    :return: The created order with updated information from the repository
    :rtype: Order
    """
    # Check if the order id already exists
    if order_repository.get_order_by_id(order.id):
        raise ValueError(f"Order with ID {order.id} already exists")
    return order_repository.create_order(order)


def get_order_by_id(order_id: int) -> Order:
    """
    Fetch the order details for a given order ID.

    This function retrieves the order information from the order repository
    based on the provided order ID.

    :param int order_id: The unique identifier for the order
    :return: The order details associated with the specified order ID
    :rtype: Order
    """
    return order_repository.get_order_by_id(order_id)


def process_order(order: Order) -> Order:
    """
    Process an order by checking stock availability and calculating the final payment details.

    Detailed processing includes:
    - Checking stock availability for each item in the order
    - Subtracting stock quantities if available
    - Calculating the price per unit and subtotal for each item
    - Summing up the total payment including taxes and discounts
    - Calculating the cash returned to the customer
    - Updating the order status based on the availability of stock and sufficient cash

    :param order: Order object containing the details to be processed
    :type order: Order
    :return: Updated Order object with processing details and status
    :rtype: Order
    """
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
                    order_in_progress.status = StatusOrder.FAILED
            else:
                # If the stock is not available, set the order status to FAILED
                is_all_rounds_processed_by_stock = False
                result_details = get_error_message_item(currentItem, currentRound)
                order_in_progress.status = StatusOrder.FAILED
                order_in_progress.cash_returned = order_in_progress.cash_tendered
    if is_all_rounds_processed_by_stock:
        # Calculate the total to pay from processed items including taxes and discounts
        order_in_progress.total_to_pay = (sum([item.sub_total for item in
                                               order_in_progress.processed_items]) + order_in_progress.taxes) - order_in_progress.discounts
        # Calculate the cash returned to the customer
        cash_returned = order_in_progress.cash_tendered - order_in_progress.total_to_pay
        order_in_progress.cash_returned = 0.0 if cash_returned < 0 else cash_returned
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
    """
    Generates an error message indicating failure to process an order due to insufficient stock
    of a specific item in a specific round.

    :param current_item: The item subtotal object which includes details about the item and its
                         stock information.
    :param current_round: The items request round object that includes the round details for
                          item requests.

    :return: A formatted error message string.
    :rtype: str
    """
    return "Order failed to process due to insufficient stock of item with id: " + str(
        current_item.id_item) + " in round with id: " + str(current_round.id)


def update_order(order_id: int, order: Order) -> Order:
    """
    Updates an existing order in the order repository.

    This function takes an order ID and an order object, updates the order in the
    repository, and returns the updated order object.

    :param order_id: The unique identifier for the order to be updated.
    :type order_id: int
    :param order: The order object containing updated information.
    :type order: Order
    :return: The updated order object.
    :rtype: Order
    """
    order_repository.update_order(order)
    return order


def delete_order(order_id: int) -> bool:
    """
    Deletes an order from the repository based on the provided order ID.

    :param order_id: The ID of the order to be deleted.
    :type order_id: int
    :return: A boolean indicating whether the order was successfully deleted.
    :rtype: bool
    """
    order_repository.delete_order(order_id)
    return True
