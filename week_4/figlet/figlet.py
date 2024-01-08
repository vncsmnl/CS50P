import sys
from pyfiglet import Figlet
import random

def parse_arguments():
    if len(sys.argv) == 1:
        return random.choice(fonts)
    elif len(sys.argv) == 3 and sys.argv[1] in ["-f", "--font"] and sys.argv[2] in fonts:
        return sys.argv[2]
    else:
        sys.exit("Invalid arguments.")

if __name__ == "__main__":
    fonts = Figlet().getFonts()

    font = parse_arguments()

    user_input = input("Enter text to display: ")
    print("Output:\n", Figlet(font=font).renderText(user_input))
