from langchain_core.tools import tool

from app.services.order_service import OrderService

service = OrderService()


@tool
def order_status(order_id: float):
    """
    Return the status of an order.
    """

    return service.get_order_status(int(order_id))


@tool
def tracking_number(order_id: float):
    """
    Return the tracking number for an order.
    """

    return service.get_tracking_number(int(order_id))


@tool
def customer_orders(customer_name: str):
    """
    Return all orders placed by a customer.
    """

    return service.list_customer_orders(customer_name)