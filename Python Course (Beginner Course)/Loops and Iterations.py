
colors = ["purple", "red", "orange", "yellow"]
for x in colors:
    print(x)

for y in "orange":
    print(y)

for z in colors:
    if z == "red":
        continue
    print(z)

for w in colors:
    print(w)
    if w == "red":
        break

v = range(8)
for u in v:
    print(u)

things = ["car", "notebook", "shirt", "shoes"]
for r in colors:
    for s in things:
        print(r, s)


i = 1
while i <= 10:
    print(i)
    i += 1

i = 0
while i < 5:
    i += 1
    if i == 4:
        continue
    print(i)

i = 1
while i < 7:
    print(i)
    i += 1
else:
    print("i is no longer less than 7.")