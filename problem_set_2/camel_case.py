#function to change camel case to snake case
def camel_to_snake(camelCase):
    snake_case = "" #set an empty variable
    for i in camelCase: #loop through the char in the string from the parameter
        if i.isupper(): #check if the char is upper case
            snake_case += "_" + i.lower() #add _ and all char lower case to var snake case
        else:
            snake_case += i #if not upper case, add all char to var snake case
    return snake_case


camelCase = input("camelCase: ").strip() #ask the user for the string, add strip to avoid unecessary spaces
snake_case = camel_to_snake(camelCase) #set the result of the function camel_to_snake in the variable snake case
print("snake_case: " + snake_case) #print the snake case string
