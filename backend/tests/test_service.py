from app.services.order_service import OrderService

service = OrderService()

print(service.get_order(1002))

print()

print(service.get_order_status(1002))

print()

print(service.get_tracking_number(1002))