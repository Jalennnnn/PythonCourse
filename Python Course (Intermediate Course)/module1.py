def greeting(name):
    print("Hey there," + name + "! Ready to do some math?")

class User:
    def __init__(self, name, age, country):
        self.name = name
        self.age = age
        self.country = country

user_1 = User("Priya", 22, "India")
user_2 = User("Anthony", 19, "Canada")
user_3 = User("Mae", 17, "Philippines")
user_4 = User("Hiroyuki", 62, "Japan")
user_5 = User("Stacy", 51, "New Zealand")

def get_sum(x, y):
    return x + y

def get_dif(x, y):
    return x - y

def get_prod(x, y):
    return x * y

def get_quo(x, y):
    return x / y

