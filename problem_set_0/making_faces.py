
#define a function to ask the user for a string and output the string as a parameter in the converted_emoji function
def main():
    string = input("")
    print (convert_emoji(string))

#define a function to convert the emojis and return the value
def convert_emoji(n):
    return n.replace(":)", "🙂").replace(":(", "🙁")

#call the main function
main()
