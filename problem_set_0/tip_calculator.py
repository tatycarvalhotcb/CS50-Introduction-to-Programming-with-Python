#main function to ask the user the values and calc the tip
def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


#function to format the dollar input value to be able to calc the tip
def dollars_to_float(d):
    dollars = d.replace("$", "")
    return float(dollars)


#function to format the percent input value to be able to calc the tip
def percent_to_float(p):
    percent = p.replace("%", "")
    return float(percent) / 100


#call the function
main()