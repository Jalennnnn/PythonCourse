shopping_list = {"weird hat": 150, "purple rug": 450,
                 "old books": 200, "stuffed elephant": 50}
print(shopping_list)

basketball_teams = {"Crouching Tigers": ["Jacob", "Kevin", "Roni", "Joshua", "Isagani"],
                    "Hidden Dragons": ["Ted", "Bryan", "Edu", "Luis", "Mark"]}
print(basketball_teams)

anime_character = {"Name": "Eren", "Age": 19, "Childhood friends": ["Armin", "Mikasa"]}
print(anime_character)

empty_dictionary = {}
print(empty_dictionary)

shopping_list = {"weird hat": 150, "purple rug": 450,
                 "old books": 200, "stuffed elephant": 50}
shopping_list["plastic ring"] = 20
shopping_list["stuffed elephant"] = 80
print(shopping_list)

pets = {"Gerald": "guinea pig", "Alice": "dog", "Ruby": "cat"}
print(pets)
pets.update({"Ron": "gecko", "Paulina": "hamster", "Marlon": "goldfish"})
print(pets)

relative = ["Tita malou", "Jeff", "Tito Roger", "Veronica"]
age = [54, 14, 55, 19]
print(relative, age)
combined_list = zip(relative, age)
print(list(combined_list))
relative_age = dict(zip(relative, age))
print(relative_age)
