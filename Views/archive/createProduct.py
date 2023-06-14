class CreateProduct:
    @staticmethod
    def create_product():
        product_id = input("Enter product id: ")
        name = input("Enter product name: ")
        price = input("Enter product price: ")
        description = input("Enter product description: ")
        category = input("Enter product category: ")
        quantity= input("Enter quantity: ")
        print("Product successfully created!")

        return product_id, name, price, description, category,quantity
