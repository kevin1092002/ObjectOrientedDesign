# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from Controllers.UserController import UserController
from Controllers.ProductController import ProductController
from Views.userView import UserView
from Views.productView import ProductView
from Views.categoryView import CategoryView

# def main():
#     user_controller = UserController()
#     action = None
#
#     while action not in ["1", "2"]:
#         action = input("What would you like to do?\n1. Login\n2. Sign up\n")
#
#     if action == "1":
#         logged_in_user = user_controller.login()
#         if logged_in_user:
#             print(f"User {logged_in_user.username} is logged in. User type: {type(logged_in_user).__name__}")
#             if(type(logged_in_user).__name__=="Customer"):
#                 print("Here is the catalog")
#                 logged_in_user.browse_catalog()
#                 search = input("Do you want to search for a product belong to a category?\n1.Yes\n2.No\n")
#                 while search == "1":
#                     category = input("Please Enter a category\n")
#                     print("Here are the product related to your category")
#                     logged_in_user.browse_product_withCategory(category)
#                     exit = input("Do you want to continue searching?\n1. Yes\n2. No\n")
#                     if exit == "2":
#                         break
#
#         else:
#             print("Login failed.")
#     elif action == "2":
#         user_controller.sign_up()
#         user_controller.login()


def main():
    user_controller = UserController()
    user_view = UserView()
    # product_controller = ProductController()
    # category_view = CategoryView()
    product_view = ProductView()
    # category_view.add_category()

    action = None
    while action not in ["1", "2"]:
        action = user_view.prompt_for_action()

    if action == "1":
        logged_in_user = user_controller.login()
        if logged_in_user:
            user_view.display_login_success(logged_in_user)

            if type(logged_in_user).__name__ == "Customer":
                product_view.display_catalog()

                while user_view.prompt_for_product_search():
                    category = user_view.prompt_for_category()
                    product_view.display_products_in_category(category)

            elif type(logged_in_user).__name__ == "Admin":
                product_view.create_product()
        else:
            user_view.display_login_failure()

    elif action == "2":
        user_controller.sign_up()

        # Use this below for a logged-in user.
        #logged_in_user = user_controller.login()


if __name__ == '__main__':
    main()


