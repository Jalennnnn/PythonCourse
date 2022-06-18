help("modules")

help("random")
print(dir("random"))

from random import randint
print(int(randint(1, 1000)))

import datetime
t =  datetime.datetime.now()
print(t)

import datetime
t = datetime.datetime(2022, 6, 18)
print(t.strftime("%B"))
print(t.year)

x = datetime.datetime(1963, 8, 28)
print(x)