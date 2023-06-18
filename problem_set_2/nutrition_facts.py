def main():
    #ask the user for a input item and set to lower case for case-insensitive and trim any adicional space with strip
    fruit = input("Item: ").lower().strip()
    #set result of the function fruit_calories, with the fruit input as a parameter, in the variable calories
    calories = fruit_calories(fruit)
    #check if calories is true and print the calories, if not, nothing will be printed
    if calories:
        print(f"Calories: {calories}")


def fruit_calories(fruit):
    #dict with all the fruits and calories
    items = {
        "apple": 130,
        "avocado": 50,
        "banana": 110,
        "cantaloupe": 50,
        "grapefruit": 60,
        "grapes": 90,
        "honeydew melon": 50,
        "kiwifruit": 90,
        "lemon": 15,
        "lime": 20,
        "nectarine": 60,
        "orange": 80,
        "peach": 60,
        "pear": 100,
        "pinapple": 50,
        "plums": 70,
        "strawberries": 50,
        "sweet cherries": 100,
        "tangerine": 50,
        "watermelon": 80
    }
    #check if parameter gave in fruit is in the dict items and return the value of calories if it's true
    if fruit in items:
        return items[fruit]

#call main function
main()
