def main():
    expression = input("Expression: ") #ask the user an arithmatic expression
    result = expression_calc(expression) #set a variable to use the input as a parameter in the calc function   
    if result: #if the calc in the function expression_calc is true/valid, output the expression result as a float formated w/ 1 decimal place
        print(float("{:.1f}".format(result)))
    else: #if the calc in the function expression_calc is false/invalid, output the the invalid expression string
        print("Invalid expression")


#function to calculate the expression that the user gave
def expression_calc(n):
    x, y, z = n.split(" ") #separate the value in the parameter into 3 variables: x, y and z
    x = int(x) #set the variable x to a integer
    z = int(z) #set the variable z to a integer
    if y == "+": #verify the operator and calculate appropriately
        return x + z
    elif y == "-":
        return x - z
    elif y == "*":
        return x * z
    elif y == "/" and z != 0: #verify also if the variable z is not equal to 0 if it's a division
        return x / z


#call the main function
main()