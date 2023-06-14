class LoginView:
    @staticmethod
    def login(controller):
        username = input("Please enter your username: ")
        password = input("Please enter your password: ")
        user = controller.get_user(username)
        
        if user and user.password == password:
            print("Successfully logged in!")
            return user
        else:
            print("Invalid credentials. Please try again.")
            return None