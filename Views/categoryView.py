from Controllers.CategoryController import CategoryController


class CategoryView:

    @staticmethod
    def add_category():
        category_id = input("Enter category id: ")
        name = input("Enter category name: ")
        description = input("Enter category description: ")
        CategoryController.add_category(category_id,name,description)
        print("Category successfully added!")