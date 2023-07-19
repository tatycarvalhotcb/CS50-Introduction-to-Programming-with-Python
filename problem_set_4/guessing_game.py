import random

#enter a positive number level and the function will generate a random number to you to guess
#if you does not enter a postive integer, the function will repromp until you do

def guess_the_number():
    while True:
        try:
            level = int(input("Level: "))
            if level > 0:
                break
        except ValueError:
            pass

    random_int = random.randint(1, level)

    while True:
        try:
            guess = int(input("Guess: "))
            if guess > 0:
                if guess < random_int:
                    print("Too small!")
                if guess > random_int:
                    print("Too large!")
                if guess == random_int:
                    print("Just right!")
                    break
        except ValueError:
            pass


guess_the_number()
