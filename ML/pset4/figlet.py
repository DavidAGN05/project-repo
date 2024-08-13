import sys
import random
from pyfiglet import Figlet
figlet = Figlet()

def main():
    if len(sys.argv) == 1:
        
        # calls to function random fonts
        text_font = rand_font()[0]



    elif len(sys.argv) == 3:  
        # checks if 1st str is -f or --font
        text_font = valid_args(sys.argv[1], sys.argv[2])
        


    else:
        sys.exit("Invalid usage")

    #converts font
    text = input("Input: ")
    figlet.setFont(font = text_font)
    print(figlet.renderText(text))
 

def rand_font():
    return random.choices(figlet.getFonts(), k = 1)
    
def valid_args(str, font):
    if str == "-f" or str == "--font":
        if font in figlet.getFonts():
            return font
        else:
            sys.exit("Invalid usage")
    else:
        sys.exit("Invalid usage")

main()
