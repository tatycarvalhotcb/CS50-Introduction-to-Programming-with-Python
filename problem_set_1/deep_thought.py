#ask the user the question
question = input("What is the Answer to the Great Question of life, the Universe, and Everything? ").lower().strip()

#use if statement to verify the user input and output Yes or No
if question == "42" or question == "forty-two" or question =="forty two":
    print("Yes")
else:
    print("No")