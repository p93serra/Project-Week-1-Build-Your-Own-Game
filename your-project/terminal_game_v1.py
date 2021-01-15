#             ________________________________________________
#            /                                                \
#           |    _________________________________________     |
#           |   |                                         |    |
#           |   |                                         |    |
#           |   |                                         |    |
#           |   |           TERMINAL MASTERMIND           |    |
#           |   |                                         |    |
#           |   |                                         |    |
#           |   |                                         |    |
#           |   |   Author: Pau Serra                     |    |
#           |   |   Version v1                            |    |
#           |   |_________________________________________|    |
#           |                                                  |
#            \_________________________________________________/
#                   \___________________________________/
#                ___________________________________________
#             _-'    .-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.  --- `-_
#          _-'.-.-. .---.-.-.-.-.-.-.-.-.-.-.-.-.-.-.--.  .-.-.`-_
#       _-'.-.-.-. .---.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-`__`. .-.-.-.`-_
#    _-'.-.-.-.-. .-----.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-----. .-.-.-.-.`-_
# _-'.-.-.-.-.-. .---.-. .-------------------------. .-.---. .---.-.-.-.`-_
#:-------------------------------------------------------------------------:
#`---._.-------------------------------------------------------------._.---'

import random
from os import system, name
from termcolor import colored

# define our clear function
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

# Function to update the board in the terminal.
def print_board(passcode, guess_codes, guess_flags):
    color_board = "magenta"
    print(colored("##########################################",color_board))
    print(colored("################  Menu  ##################",color_board))
    print(colored("##########################################",color_board))
    print(colored("#  Using numbers enter code:             #",color_board))
    print(colored("#   ",color_board), colored("4 - BLUE  ", "blue"),
        colored("5 - WHITE ", "white"), colored("6 - CYAN ", "cyan"),
        colored("    #",color_board))
    print(colored("#   ",color_board), colored("1 - RED   ", "red"),
        colored("2 - GREEN ", "green"), colored("3 - YELLOW ", "yellow"),
        colored("  #",color_board))
    print(colored("##########################################",color_board))
    print(colored("############    IRONHACK    ##############",color_board))
    print(colored("############   MASTERMIND   ##############",color_board))
    print(colored("##########################################",color_board))
    print(colored("# R W #", color_board), end="")

    for x in passcode:
        if x != "?¿?":
            print("\t  ", colored(x[:3], x.lower()), end="")
        else:
            print("\t  ", x[:3], end="")
    print(colored("   #",color_board))

    for i in reversed(range(len(guess_codes))):
        print(colored("##########################################",
            color_board))
        print(colored("#",color_board), guess_flags[i][0],
            guess_flags[i][1], end="")
        print(colored(" #",color_board), end="")
        for x in guess_codes[i]:
            if x != "***":
                print("\t  ", colored(x[:3], x.lower()), end="")
            else:
                print("\t  ", x[:3], end="")
        print(colored("   #",color_board))
    print(colored("##########################################",color_board))

def startGame(repeat = 0, dummy = 0, chances = 10):
    colors = ["RED", "GREEN", "YELLOW", "BLUE", "WHITE", "CYAN"]

    colors_map = {1:"RED", 2:"GREEN", 3:"YELLOW", 4:"BLUE", 5:"WHITE",
        6:"CYAN"}

    if dummy == 1:
        passcode = ["RED", "GREEN", "YELLOW", "BLUE"]
    elif dummy == 0:
        if repeat == 0:
            random.shuffle(colors)
            passcode = colors[:4]
        elif repeat == 1:
            passcode = random.choices(colors, k=4)
        else:
            print("Wrong repeat parameter!!! Only 0 or 1")
            return None
    else:
        print("Wrong dummy parameter!!! Only 0 or 1")
        return None

    show_passcode = ['?¿?', '?¿?', '?¿?', '?¿?']

    guess_codes = [['***', '***', '***', '***'] for x in range(chances)]

    guess_flags = [['*', '*'] for x in range(chances)]

    clear()

    turn = 0

    # GAME LOOP
    while turn < chances:
        print_board(show_passcode, guess_codes, guess_flags)

        try:
            code = list(map(int, input("Enter your guess = ").split()))
        except ValueError:
            clear()
            print(colored("Wrong format!! You should use only integers!!",
                "white", "on_red"))
            continue

        if len(code) != 4:
            clear()
            print(colored("Wrong length!! Should guess 4 colors.", "white",
                "on_red"))
            continue

        err = 0
        for x in code:
            if x > 6 or x < 1:
                err = 1

        if err == 1:
            clear()
            print(colored("Wrong code!! Should choose numbers between 1-6",
                "white", "on_red"))
            continue

        for i in range(4):
            guess_codes[turn][i] = colors_map[code[i]]

        dummy_passcode = [x for x in passcode]

        pos = 0

        guess_flags[turn][0] = 0
        guess_flags[turn][1] = 0

        for x in code:
            if colors_map[x] in dummy_passcode:
                if code.index(x) == passcode.index(colors_map[x]):
                    guess_flags[turn][0] += 1
                else:
                    guess_flags[turn][1] += 1
                dummy_passcode.remove(colors_map[x])

        # Win condition
        if guess_codes[turn] == passcode:
            clear()
            print_board(passcode, guess_codes, guess_flags)
            print(colored("Congratulations!! YOU WIN!!!!", "white", "on_green",
                attrs=['blink']))
            break

        turn += 1
        clear()

        # Lose condition
        if turn == chances:
            clear()
            print_board(passcode, guess_codes, guess_flags)
            print(colored("YOU LOSE!!! Better luck next time!!!", "white",
                "on_red", attrs=['blink']))
