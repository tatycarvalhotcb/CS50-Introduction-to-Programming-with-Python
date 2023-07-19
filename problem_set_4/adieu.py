import inflect

p = inflect.engine()

names = []

while True:
    try:
        name = input("Names: ")
        names.append(name)
    except EOFError:
        break

list_names = p.join(names)

print(f"Adieu, adieu, to {list_names}")