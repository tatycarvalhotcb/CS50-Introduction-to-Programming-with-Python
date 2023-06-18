def no_vowels(str):
    vowels = "aeiouAEIOU" #set a variable with the vowels in lower and upper case
    for v in str: #loop in the str chars
        if v in vowels: #if the char is in the vowels variable
            str = str.replace(v, "") #replace the vowel for no char
    print(f"Output: {str}") #output the new str

str = input("Input: ") #ask the user for the string
no_vowels(str) #call the function with the user's input str as a parameter