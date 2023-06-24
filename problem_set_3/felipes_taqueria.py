def order_felipes_taqueria():
    #dict with all the menu items
    menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
    }

    #set a variable with an empty list
    order = []
    #set a variable with value 0
    total_cost = 0.0

    #loop through the input so the user can be reprompt for more items
    while True:
        try:
            #set a variable with the user input, use strip to avoid extra spaces, lower to be case insensitively and title to be like the menu items format
            item = input("Item: ").strip().lower().title()
            #check if item from input is not in the menu, skip and reprompt
            if item not in menu:
                continue
            #add item from input in the list of the variable order
            order.append(item)
            #sum the item cost in the variable total_cost
            total_cost += menu[item]
            #print the total_cost formated with 2 decimal places
            print(f"Total ${total_cost:.2f}")
        #break the loop if there is an error
        except EOFError:
            break

#call the function
order_felipes_taqueria()