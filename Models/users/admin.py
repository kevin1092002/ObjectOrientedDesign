# out of assignment 3 scope
from .user import User


class Admin(User):

    # Constructor
    def __init__(self, user_id, username, password, email, address, phone_number, user_type):
        super().__init__(user_id, username, password, email, address, phone_number, user_type)

    # Admin can manage products
    def manage_products(self):
        # Implement functionality for managing products in the store
        pass

    # Outside of assignment 3 scope.
    def manage_orders(self):
        # Implement functionality for managing customer orders
        pass

    # Outside of assignment 3 scope.
    def manage_users(self):
        # Implement functionality for managing users (customers, staff, etc.)
        pass