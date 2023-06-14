# Out of Assignment 3 Scope
from sale.invoice import Invoice


class Order:
    def __init__(self, order_id, state, state_description, products, total_balance, customer_id, customer_name, customer_shipping):
        self.order_id = order_id
        self.state = state
        self.state_description = state_description
        self.products = products
        self.total_balance = total_balance
        self.customer_id = customer_id
        self.customer_name = customer_name
        self.customer_shipping = customer_shipping
        self.invoice = self.create_invoice()

    def create_invoice(self):
        # I thought it was a cool idea to add INV- before the id. cbf doing it for order :p
        invoice_id = f"INV-{self.order_id}"
        return Invoice(invoice_id, self.total_balance, self.products, self.customer_id, self.customer_name)

    def send_receipt(self):
        pass  # logic to send the receipt
