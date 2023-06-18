#define a function to ask the user the mass as a int and output the calculation with eistein_calc using the input as parameter
def main():
    mass = int(input("m: "))
    print (eistein_calc(mass))

#define a function to calc the mass and return the of E
def eistein_calc(n):
    E = n*(300000000**2)
    return E

#call the main function
main()