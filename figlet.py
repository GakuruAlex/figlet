from pyfiglet import Figlet
from random import randint
import sys
def main()-> None:
    figlet_t = Figlet()
    if len(sys.argv) > 1:
        font: str = sys.argv[2]
        flag: str = sys.argv[1]
        if flag not in ["-f", "--font"]:
            print("Invalid usage")
            sys.exit(1)
        else:
            if font in figlet_t.getFonts():
                figlet_to_use = Figlet(font=font)
        
                user_str = input("Input: ")
                print(f"Output: {figlet_to_use.renderText(user_str)}")
            else:
                print("Invalid usage")
                sys.exit(1)
    else:
        random_int = randint(0, len(figlet_t.getFonts()))
        font = figlet_t.getFonts()[random_int]
        figlet_to_use = Figlet(font=font)
        
        user_str = input("Input: ")
        print(f"Output: {figlet_to_use.renderText(user_str)}")

if __name__ == "__main__":
    main()