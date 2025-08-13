#Exercise 1: Print a dictionary with lists
#Exercise 2: Print a dictionary containing other dictionaries
#By:   Silvana Paredes
#Date: 09/08/2025

#Dictionary with lists
foods = {
    "fruits": ["apple", "pear", "banana"],
    "vegetables": ["carrot", "broccoli"],
    "meats": ["chicken", "beef"]
}

#Dictionary with other dictionaries
foods_dict = {
    "fruits": {
        "apple": "red",
        "pear": "green",
        "banana": "yellow"
    },
    "vegetables": {
        "carrot": "orange",
        "broccoli": "green"
    },
    "meats": {
        "chicken": "white",
        "beef": "red"
    }
}

#Exercise 1
print("Exercise 1")
#Print all the keys in the dictionary
for food in foods:
    print(food)

#Print each key with its corresponding list of items
for id, food in foods.items():
    print(id, food)

#Print only the lists of items (values) without keys
for food in foods.values():
    print(food)


#Exercise 2
print("Exercise 2")
#Print all the dictionary
for category, items_dict in foods_dict.items():
    print(f"{category}:")
    for item, color in items_dict.items():
        print(f"  {item} is {color}")

        
