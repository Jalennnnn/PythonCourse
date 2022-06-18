# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

name = input("Enter your name: ")
print("Hi, " + name + "!")

num1 = int(input("Please enter your first number: "))
num2 = int(input("Please enter your second number: "))
print("Your two numbers are:", num1, "and", num2)

def addNum(num1, num2):
    total = num1 + num2
    return (total)
num1 = int(input("Please enter your first number: "))
num2 = int(input("Please enter your second number: "))
print("Total:", addNum(num1, num2))