# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from Controllers.UserController import UserController
from Views.userView import UserView
from Views.productView import ProductView
from Views.categoryView import CategoryView


def main():
    user_controller = UserController()
    user_view = UserView()
    product_view = ProductView()

    action = None
    while action not in ["1", "2"]:
        action = user_view.prompt_for_action()

    if action == "1":
        logged_in_user = user_controller.login()
        if logged_in_user:
            user_view.display_login_success(logged_in_user)

            # Customer action
            if type(logged_in_user).__name__ == "Customer":
                product_view.display_catalog()

                while user_view.prompt_for_product_search():
                    category = product_view.prompt_for_category()
                    product_view.display_products_in_category(category)

            elif type(logged_in_user).__name__ == "Admin":
                while True:  # create a loop for admin actions
                    action = user_view.admin_create_item_prompt()  # update the action based on admin's input
                    if action == "1":
                        product_view.create_product()
                    elif action == "2":
                        CategoryView.add_category()
                    elif action == '3':
                        break
                    else:
                        break  # exit the loop when admin's action is not 1 or 2

        else:
            user_view.display_login_failure()

    elif action == "2":
        user_controller.sign_up()


if __name__ == '__main__':
    main()


