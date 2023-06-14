# Out of Assignment 3 Scope
import datetime


class Invoice:
    def __init__(self, invoice_id, amount_paid, products, customer_id, customer_name):
        self.invoice_id = invoice_id
        self.amount_paid = amount_paid
        self.products = products
        self.customer_id = customer_id
        self.customer_name = customer_name
        self.date_of_purchase = datetime.datetime.now()