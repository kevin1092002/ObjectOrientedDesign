from Models.inventory.product import Product


import csv


def re_open_file():
    file = open('Database/products.csv','r',encoding='utf8')
    reader = csv.DictReader(file)
    return reader


class ProductController:
    @staticmethod
    def create_product(product_id, name, price, description, category, quantity):
        product = Product(product_id, name, price, description, category, quantity)
        product.save()

    def update_product(self, product_id, *args):
        pass  # Implement product update logic

    def delete_product(self, product_id):
        pass  # Implement product deletion logic

    def get_product(self, product_id):
        pass  # Implement getting product details logic

    def create_category(self, *args):
        pass  # Implement category creation logic

    def update_category(self, category_id, *args):
        pass  # Implement category update logic

    def delete_category(self, category_id):
        pass  # Implement category deletion logic

    def get_category(self, category_id):
        pass  # Implement getting category details logic

    @staticmethod
    def read_all_products_from_database():
        # Implement browsing the store's product catalog
        reader = re_open_file()
        for row in reader:
            print(row)
        pass

    @staticmethod
    def read_products_related_category(category):
        # Implement browsing the store's products when customer search for Category
        reader = re_open_file()
        n=0
        for row in reader:
            if row["Category"] == category:
                print(row)
                n = n+1
        return n
        pass
