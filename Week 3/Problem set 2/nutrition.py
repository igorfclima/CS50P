fruits = {
    "apple": 130,
    "banana": 110,
    "grapefruit": 60,
    "honeydew melon": 60,
    "lemon": 15,
    "nectarine": 60,
    "peach": 60,
    "pineapple": 60,
    "strawberries": 50,
    "tangerine": 50,
    "avocado": 50,
    "cantaloupe": 50,
    "grapes": 90,
    "kiwifruit": 90,
    "lime": 20,
    "orange": 80,
    "pear": 100,
    "plums": 70,
    "sweet cherries": 100,
    "watermelon": 80
}

new_fruit = input("Item: ").strip().lower()

if new_fruit in fruits:
    new_fruit = fruits.get(new_fruit)
    print(f"Calories: {new_fruit}")
