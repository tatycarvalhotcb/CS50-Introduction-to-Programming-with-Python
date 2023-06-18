def main():
    #aks the user for a input place string
    plate = input("Plate: ")
    #check if meets all the conditions in the function is_valid
    if is_valid(plate):
        print("Valid")
    #if not, print invalid
    else:
        print("Invalid")


def is_valid(s):
#set the parameter input to be upper case and strip any adicional spaces
    s = s.upper().strip()
#check if the len is min 2 and max 6
    if len(s) >= 2 and len(s) <= 6:
#check if starts with at least 2 letters
        if s[0].isalpha() and s[1].isalpha():
#check if there are just numbers and letters
            if all(char.isalpha() or char.isdigit() for char in s):
#check if there are numbers, if they are in the end and the first number can't be 0
                for char in range(len(s)):
                    if s[char].isdigit():
                        if not s[char:].isdigit():
                            return False
#return false if the first number is 0
                char = 0
                while char < len(s):
                    if s[char].isdigit() == True:
                        if s[char] == "0":
                            return False
                        else:
                            break
                    char += 1
#return true if all conditions are true
                return True
main()

