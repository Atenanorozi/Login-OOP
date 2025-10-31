import os 

class User:
    def __init__(self, username, password):
        self.username = username
        self.passsword = password


class UserFileManager:
    def __init__(self, filename="users.txt"):
        self.filename = filename

    def load_users(self):
        users = {}
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                for line in file:
                    line = line.strip()
        return users



class Signup:
    def __init__(self, users, file_manager):
        self.users = users
        self.file_manager = file_manager

    def signup_user(self, username, password):
        if username in self.users:
            print("This username was already exists.")
        else:
            self.users[username] = User(username, password)
            print("Registration was successful.")

            
class Login:
    def __init__(self, users):
        self.users = users

    def login_user(self, username, password):
        user = self.users.get(username)
        if user and user.password == password :
            print(f"wellcome, {username}")
        else:
            print("username or password is incorrect.")


            
class SystemManager:
    def __init__(self):
        self.file_manager = UserFileManager()
        self.users = self.file_manager.load_users()
        self.signup = Signup(self.users, self.file_manager)
        self.login = Login(self.users)


if __name__ =="__main__":
    system = SystemManager()

    while True:
        print("\n*** login system ***")
        print("1. signup")
        print("2. login")
        print("3. exit")
        choice = input("Enter your choice :")

        if choice == "1":
            username = input("username :")
            password = input("password :")
            system.signup.signup_user(username, password)

        if choice == "2":
            username = input("username :")
            password = input("password :")
            system.login.login_user(username, password)

        elif choice == "3":
            print("GOODBY")
            break
        else:
            print("The option is invalid.")

