# Outside of assignment 3 scope.
from .user import User


class Customer(User):
    def __init__(self, user_id, username, password, email, address, phone_number, user_type):
        super().__init__(user_id, username, password, email, address, phone_number, user_type)

    def add_to_cart(self, product):
        # adding a product to the customer's shopping cart
        pass

    def make_order(self):
        #  occurs when a product is added for first time
        pass

    def set_shipping(self, shipping):
        self.shipping = shipping

    def update_shipping(self):
        # Implement the code to update shipping details in a cart/order
        # (instead of taking from the account if None)
        pass
