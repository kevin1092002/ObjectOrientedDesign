import csv


class Product:
    def __init__(self, product_id, name, price, description, category,quantity):
        self.product_id = product_id
        self.name = name
        self.sale_price = price
        self.description = description
        self.product_category = category
        self.quantity = quantity

    def save(self, filename='Database/products.csv'):
        with open(filename, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([self.product_id, self.name, self.sale_price,
                             self.description, self.product_category,self.quantity])