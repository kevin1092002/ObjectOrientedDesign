
class UserView:
    @staticmethod
    def input_details():
        username = input("Enter Username: ")
        password = input("Enter Password: ")
        email = input("Enter Email: ")
        address = input("Enter Address: ")
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


