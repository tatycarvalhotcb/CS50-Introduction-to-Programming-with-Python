from pyfiglet import Figlet
import sys
import random

figlet = Figlet()
fonts = figlet.getFonts()


if len(sys.argv) == 1:
    str = input("Input: ")
    random_font = Figlet(font=random.choice(fonts))
    print(random_font.renderText(str))

elif len(sys.argv) == 3:
    if sys.argv[1] == "-f" or sys.argv[1] == "--font":
        if sys.argv[2] in fonts:
            str = input("Input: ")
            selected_font = Figlet(font=sys.argv[2])
            print(selected_font.renderText(str))
        else:
            sys.exit("Invalid usage")
    else:
        sys.exit("Invalid usage")
else:
    sys.exit("Invalid usage")
