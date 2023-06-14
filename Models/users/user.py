# Adding login and maybe logout instead of authentication for the other users.
# justified in document.
import csv


class User:

    def __init__(self, user_id, username, password, email, address, phone_number, user_type):
        self.user_id = None # User is assigned a new ID from the save function
        self.username = username
        self.password = password
        self.email = email
        self.address = address
        self.phone_number = phone_number
        self.user_type = user_type

    def login(self):
        pass

    def logout(self):
        pass

    def save(self):
        with open('Database/users.csv', 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            user_ids = [int(row['user_id']) for row in reader if row['user_id'].strip()]
            self.user_id = max(user_ids) + 1 if user_ids else 1

        with open('Database/users.csv', 'a', newline='') as csvfile:
            fieldnames = ['user_id', 'username', 'password', 'email', 'address', 'phone_number', 'user_type']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writerow(
                {'user_id': self.user_id, 'username': self.username, 'password': self.password,
                 'email': self.email, 'address': self.address, 'phone_number': self.phone_number,
                 'user_type': self.user_type})

    @classmethod
    def get(cls, user_id):
        for user in cls.users:
            if user.user_id == user_id:
                return user
        return None

    @classmethod
    def delete(cls, user_id):
        for idx, user in enumerate(cls.users):
            if user.user_id == user_id:
                cls.users.pop(idx)
                return True
        return False







