import csv

from Models.users.admin import Admin
from Models.users.customer import Customer
from Models.users.staff import Staff
from Models.users.user import User
from Views.userView import UserView


class UserController:

    # Constructor
    def __init__(self):
        self.view = UserView()

    # Creating a new user
    @staticmethod
    def create_user(user_type, *args):
        if user_type == "admin":
            # check if there's already an admin
            if User.get(1) is not None:
                raise ValueError("An admin already exists")
            user = Admin(*args)
        elif user_type == "customer":
            user = Customer(*args)
        else:
            raise ValueError("Invalid user type")

        user.save()
        return user

    # Update an User object

    @staticmethod
    def update_user(user_id, *args):
        user = User.get(user_id)

        if user:
            # save attributes
            user.save()
            return user
        else:
            raise ValueError("User not found")

    # Delete a User by ID
    @staticmethod
    def delete_user(user_id):
        user = User.get(user_id)
        if user:
            user.delete()
            return
        else:
            raise ValueError("User not found")

    # Return a User by ID
    @staticmethod
    def get_user(user_id):
        user = User.get(user_id)

        if user:
            return user
        else:
            raise ValueError("User not found")

    # Sign up user and put this new user to
    # database (user.csv file in this project)
    def sign_up(self):
        username, password, email, address, phone_number = self.view.input_details()
        new_user = User(None, username, password, email, address, phone_number, "customer")
        new_user.save()  # the save method  handles assigning an ID and writing to the file.

        self.view.sign_up_successful()

    # Login a User if a user enter correct data as
    # stored in database (user.csv file in this project)
    def login(self):
        username, password = self.view.input_credentials()

        with open('Database/users.csv', 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['username'].strip() == username and row['password'].strip() == password:
                    # User is logged in successfully.
                    # Create user object and return it.

                    if row['user_type'].strip() == "admin":
                        logged_in_user = Admin(row['user_id'], row['username'], row['password'], row['email'],
                                               row['address'], row['phone_number'],row['user_type'])
                        self.view.admin_login_successful()  # if it's an admin user, notify them of admin login.
                    else:
                        logged_in_user = Customer(row['user_id'], row['username'], row['password'], row['email'],
                                              row['address'], row['phone_number'],row['user_type'])
                        self.view.login_successful()  # if it's a non-admin user it is a customer in our implementation.

                    return logged_in_user

            self.view.invalid_username_password()

        return None






