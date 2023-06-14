# Outside of assignment 3 scope.
from .user import User

# Outside of assignment 3 scope - No Staff anymore.


class Staff(User):
    def __init__(self, username, password, email, staff_id):
        super().__init__(username, password, email)
        self.staff_id = staff_id

    # Outside of assignment 3 scope.
    def process_orders(self):
        #  Functionality for processing customer orders
        pass

    # Outside of assignment 3 scope.
    def update_inventory(self):
        # Implement functionality for updating the store's inventory
        pass
