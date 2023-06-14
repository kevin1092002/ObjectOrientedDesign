class RegisterView:
    @staticmethod
    def register(controller):
        user_id = 1 
        user_type = input("1: Admin, 2: Staff, 3: Customer: ")
        if user_type == '1':
            user_type = "admin"
        if user_type == '2':
            user_type = "staff"
        if user_type == '3':
            user_type = "customer"
        
        username = input("Please enter your username: ")
        password = input("Please enter your new password: ")
        email = input("Please enter your email: ")
        address = input("Please enter your address: ")
        phone_number = input("Please enter your phone number: ")

        print('User successfully registered!')
        return [user_type, user_id, username, password, email, address, phone_number]
   