# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import module1

module1.greeting("Jalen")

a = module1.user_1
print("Hey there, " + a.name + "! Ready to do some math?")
c = module1.user_3
print("Hey there, " + c.name + "! Ready to do some math?")

import module1 as m1
a = m1.user_1
print("Hey there, " + a.name + "! Ready to do some math?")

import module1
sum = module1.get_sum(4591, 782)
print(sum)
quotient = module1.get_quo(100, 22)
print(quotient)

from module1 import *
product = get_prod(9, 4)
print(product)

from module1 import get_dif
difference = get_dif(296, 57)
print(difference)

from functionfile import personal_greeting
from functionfile import your_province

personal_greeting("Anna")
your_province("Pampanga")
