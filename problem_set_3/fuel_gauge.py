def main():
    #set a main function to return the fuel_gauge function stored in the variable tank
    tank = fuel_gauge() 
    return tank


def fuel_gauge():
    #loop through the input so if the input doesn't match the requeriment, it prompt again
    while True: 
        try:
            #ask the fraction to user, strip to avoid any adicional spaces and set in a variable fraction
            fraction = input("Fraction: ").strip() 
            #separate the input in the variable fraction using the "/" as a separator into variables int1 and int2
            int1, int2 = fraction.split("/") 
            #set int1 and int2 to a integer so it can use in the calculation
            int1 = int(int1) 
            int2 = int(int2) 
            #calculate the division between fraction values, transform the value into a whole decimal number multiplying by 100 and using round
            fraction_value = round(int1 / int2 * 100) 
            #check if int1 is greater than int2
            if int1 > int2:
                #if true, skip and prompt again 
                continue 
        except (ValueError, ZeroDivisionError):
            #if there is an error, skip and prompt again
            pass 
        else:
            #else if all conditions are false, break the loop
            break 
    
    #check if value is greater or equal to 99
    if fraction_value >= 99: 
        #print F as Full
        print("F") 
    #check if value is less or equal to 
    elif fraction_value <= 1: 
        #print E as Empty
        print("E") 
    else:
        #else if all conditions are false, print the value + %
        print(f"{fraction_value}%") 


#call the main function
main()