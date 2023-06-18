def coke_machine():
    amount_due = 50 #set the whole amount in the variable
    while amount_due > 0: #loop while amount is greater than 0
        print(f"Amount Due: {amount_due}") #show the amount
        coin = int(input("Insert Coin: ")) #ask user the coin value
        if coin == 25 or coin == 10 or coin == 5: #check if coin is valid
            amount_due -= coin #if it is, subtract coin from amount
            if amount_due <= 0: #check if amount is less or equal to 0
                print(f"Change Owed: {abs(amount_due)}") #show the difference amount - coin as a change, use abs to not show negative value

#call function
coke_machine()

