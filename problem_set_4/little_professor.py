import random


def main():
    level = get_level()
    score = 0

    for i in range(10):
        random_problem = generate_integer(level)
        result = random_problem[0] + random_problem[1]
            
        tries = 0
        while tries < 3:
            try:
                answer = int(input(f"{random_problem[0]} + {random_problem[1]} = "))
                if answer == result:
                    score += 1
                    break
                else:
                    tries += 1
                    print("EEE")
            except ValueError:
                print("EEE")
        else:
            print(f"{random_problem[0]} + {random_problem[1]} = {result}")
    
    print(f"Score: {score}")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level > 0 and level <= 3:
                break
        except ValueError:
            pass

    return level   


def generate_integer(level):
    if level == 1:
        random_x = random.randint(0,9)
        random_y = random.randint(0,9)
    elif level == 2:
        random_x = random.randint(10,99)
        random_y = random.randint(10,99)
    else:
        random_x = random.randint(100,999)
        random_y = random.randint(100,999)
        
    return random_x, random_y


if __name__ == "__main__":
    main()