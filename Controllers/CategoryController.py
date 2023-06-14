from Models.inventory.productCategory import ProductCategory


class CategoryController:
    @staticmethod
    def add_category(category_id, name, description):
        category = ProductCategory(category_id, name, description)
        category.save()
        pass
