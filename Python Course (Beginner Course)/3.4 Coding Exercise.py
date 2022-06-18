class Customers:
    greeting = "Welcome to the Coffee place!"

c_1 = Customers()
c_2 = Customers()

c_1.name = "Samirah"
c_2.name = "Jerry"
c_1.beverage = "Iced caffe latte"
c_2.beverage = "Caramel macchiato"
c_1.food = "Cinnamon roll"
c_2.food = "Glazed Doughnut"
c_1.total = 225
c_2.total = 230
print(Customers.greeting)
print(c_1.name, "and", c_2.name)
print("what does Samirah want to drink?", c_1.beverage)
print("what does Jerry want to eat?", c_2.food)
