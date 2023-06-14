from Controllers.ProductController import ProductController

import csv


# helper method to list all the category to choose
def get_categories():
    with open('Database/category.csv', 'r', encoding='utf8') as file:
        category_reader = csv.DictReader(file)
        return [row["Category_Name"] for row in category_reader]


# helper method to input a category
def input_categories():
    categories = get_categories()
    try:
        for idx, cat in enumerate(categories, start=1):
            print(f'{idx}. {cat}')
        category_index = int(input("Enter the number of the category: ")) - 1
        return categories[category_index]
    except IndexError:
        print("Please only choose a number from the list of category above")
        return input_categories()
    except BaseException:
        print("Please only enter a number")
        return input_categories()


class ProductView:
    @staticmethod
    def prompt_for_category():
        return input_categories()

    @staticmethod
    def create_product():
        product_id = input("Enter product id: ")
        name = input("Enter product name: ")
        price = input("Enter product price: ")
        description = input("Enter product description: ")
        
        # Show the list of available categories
        category = input_categories()
        quantity = input("Enter quantity: ")

        ProductController.create_product(product_id, name, price, description, category, quantity)
        print("Product successfully created!")

    @staticmethod
    def display_catalog():
        print("Here is the catalog")
        ProductController.read_all_products_from_database()

    @staticmethod
    def prompt_for_product_search():
        return input("Do you want to search for a product "
                     "belong to a category?\n1.Yes\n2.No\n") == "1"

    @staticmethod
    def display_products_in_category(category):
        print("Here are the products related to your category")
        if ProductController.read_products_related_category(category) == 0:
            print("There is no products in this category yet")
        pass
