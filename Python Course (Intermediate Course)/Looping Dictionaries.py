employee_1 = {"Name": "Frank", "Position": "Sales Representative", "Email Address": "frank@company.com"}
for key, value in employee_1.items():
    print(key)
    print(value)

character_weapons = {"Harry Potter": "wand", "Percy Jackson": "Riptide",
                     "Katniss Everdeen": "bow and arrow", "Bilbo Baggins": "ring"}
for name in character_weapons.keys():
    print(name)

for name in character_weapons.keys():
    if name == "Percy Jackson":
        continue
    print(name)

most_delicious = {"Mcdonald's": ["fried chicken", "sundae"], "Jollibee": ["fried chicken", "spaghetti"],
                  "KFC": ["gravy", "mashed potatoes"], "Pizza Hut": ["pizza", "pasta"]}
for item in most_delicious.values():
    print(item)
