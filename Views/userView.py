import csv
import re


class UserView:

    @staticmethod
    def validate_username(username):
        if not username.isalpha():
            return False
        return True

    @staticmethod
    def validate_phone_number(phone_number):
        # Phone numbers should be digits and 10 long.
        if not phone_number.isdigit() or len(phone_number) != 10:
            return False
        return True

    @staticmethod
    def validate_email(email):
        # Email addresses must contain an @.
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            return False
        return True

    @staticmethod
    def input_details():
        username = input("Please Enter your username: ")
        while not UserView.validate_username(username):
            print("Invalid username! Usernames should not contain numbers.")
            username = input("Enter Username: ")
        password = input("Enter Password: ")

        email = input("Please enter your email address: ")
        while not UserView.validate_email(email):
            print("Invalid email! Please ensure your email contains an '@' followed by a domain (e.g. 'example.com').")
            email = input("Enter Email: ")
        address = input("Enter Address: ")

        phone_number = input("Please Enter your phone number: ")
        while not UserView.validate_phone_number(phone_number):
            print("Invalid phone number! Phone numbers must contain 10 digits.")
            phone_number = input("Enter Phone Number: ")
        return username, password, email, address, phone_number

    @staticmethod
    def input_credentials():
        username = input("Enter Username: ")
        password = input("Enter Password: ")
        return username, password

    @staticmethod
    def sign_up_successful():
        print("You have successfully signed up!")

    @staticmethod
    def login_successful():
        print("Login has been successful!")

    @staticmethod
    def admin_login_successful():
        print("Login Successful! Welcome, Admin!")
        pass

    @staticmethod
    def invalid_username_password():
        print("Invalid username or password!")

    @staticmethod
    def prompt_for_action():
        return input("What would you like to do?\n1. Login\n2. Sign up\n")

    @staticmethod
    def display_login_success(user):
        print(f"User {user.username} is logged in. User type: {type(user).__name__}")

    @staticmethod
    def display_login_failure():
        print("Login failed.")

    @staticmethod
    def prompt_to_continue_searching():
        return input("Do you want to continue searching?\n1. Yes\n2. No\n")

    @staticmethod
    def admin_create_item_prompt():
        return input('What would you like to do?\n1. Create Product\n2. Create Category\n3. Exit\n')

    @staticmethod
    def prompt_for_category():
        with open('Database/category.csv', 'r', encoding='utf8') as file:
            print("Please choose a category from the list below and please matches the case")
            category_reader = csv.DictReader(file)
            for rows in category_reader:
                print(rows["Category_Name"])
        return input()

    @staticmethod
    def prompt_for_product_search():
        user_input = input("Do you want to search for a "
                           "product belong to a category?\n1.Yes\n2.No\n")
        while user_input != "1" and user_input != "2":
            print("please enter 1 or 2")
            user_input = input("Do you want to search for a "
                               "product belong to a category?\n1.Yes\n2.No\n")
        return user_input == "1"
