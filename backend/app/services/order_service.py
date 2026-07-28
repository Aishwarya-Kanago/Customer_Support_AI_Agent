from app.repositories.order_repository import OrderRepository


class OrderService:

    def __init__(self):

        self.repository = OrderRepository()

    def get_order(self, order_id: int):

        order = self.repository.get_order(order_id)

        if order is None:

            return {
                "success": False,
                "message": f"Order {order_id} not found."
            }

        return {
            "success": True,
            "data": order
        }

    def get_order_status(self, order_id: int):

        result = self.get_order(order_id)

        if not result["success"]:
            return result

        return {
            "success": True,
            "order_id": order_id,
            "status": result["data"]["status"]
        }

    def get_tracking_number(self, order_id: int):

        result = self.get_order(order_id)

        if not result["success"]:
            return result

        status = result["data"]["status"]

        if status == "Cancelled":

            return {
                "success": False,
                "message": "Cancelled orders do not have tracking numbers."
            }

        return {
            "success": True,
            "order_id": order_id,
            "tracking_number": result["data"]["tracking_number"]
        }

    def list_customer_orders(self, customer_name: str):

        orders = self.repository.list_customer_orders(customer_name)

        return {
            "success": True,
            "customer": customer_name,
            "orders": orders
        }