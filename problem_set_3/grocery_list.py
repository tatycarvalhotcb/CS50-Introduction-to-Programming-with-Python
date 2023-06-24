def grocery_list():
    #set a variable with an empty list for quantity and items
    quantity = []
    items = []

    #loop through the input so the user can be reprompt for more items
    while True:
        try:
            #set a variable with the user input, use strip to avoid extra spaces and lower to be case insensitively
            item = input("").strip().lower()
            #check if input is not in items list
            if item not in items:
                #if true, add 1 to quantity list and item to items list
                quantity.append(1)
                items.append(item)
            #check if input is in items list
            elif item in items:
                #if true, set index var to find where the item is in the list and add +1 to the quantity
                index = items.index(item)
                quantity[index] += 1
        #break the loop if inputted control-d
        except EOFError:
            break

    #set a variable with empty dict to add the quantity and items list
    dict_grocery = {}
    #loop through the quantity and items values
    for q, i in zip(quantity, items):
        #set to the dict with q(quantity) as the key and i(items) as the value
        dict_grocery[i] = q

    #sort the dict in alphabetic way
    sorted_items = sorted(dict_grocery.items())

    #loop through the the sorted_dict and print the key and value in uppercase
    for i, q in sorted_items:
        print(q, i.upper())


#call the function
grocery_list()