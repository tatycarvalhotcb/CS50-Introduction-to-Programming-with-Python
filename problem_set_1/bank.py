#ask user the greeting
greeting = input("Greeting: ").lower().strip()

#verify the greeting input and output accord with
if greeting.startswith("hello"):
    print("$0")
elif greeting.startswith("h") and not greeting.startswith("hello"):
    print("$20")
else:
    print("$100")