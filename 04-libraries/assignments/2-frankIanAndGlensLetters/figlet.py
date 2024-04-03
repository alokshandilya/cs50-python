import random
import sys
from pyfiglet import Figlet


def print_figlet():
    figlet = Figlet()

    if len(sys.argv) == 1:
        figlet.setFont(font=random.choice(figlet.getFonts()))
        text_input = get_input()
        print(figlet.renderText(text_input))
    elif len(sys.argv) == 3:
        if sys.argv[2] not in figlet.getFonts():
            sys.exit("invalid font")
        elif sys.argv[1] == "-f" or sys.argv[1] == "--font":
            text_input = get_input()
            figlet.setFont(font=sys.argv[2])
            print(figlet.renderText(text_input))
        else:
            sys.exit("wrong syntax")
    else:
        sys.exit("too many arguments")


def get_input():
    text_input = input("Input: ")
    return text_input


if __name__ == "__main__":
    print_figlet()
