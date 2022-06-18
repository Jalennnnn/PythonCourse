class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def display1(self):
        print("Username: ", self.username)
        print("Password: ", self.password)

class Admin(User):
    def __init__(self, username, password, code):
        self.code = code
        super().__init__(username, password)

    def display3(self):
        super().display1()
        print("Code:",self.code)

a_1 = Admin("leslie2001", "password1234", 2468)
a_1.display3()