import sys
from common import *
from blackjack import BlackJack

def MainMenu():
    """
    Prints the main menu and returns the users choice
    :returns: the users choice
    """
    print("1. Blackjack")
    print("2. Quit")
    return intInput("[]: ", 1, 2)

if __name__ == "__main__":
    # Entrypoint
    while True:
        choice = MainMenu()
        if choice == 1:
            game = BlackJack()
            game.play()
        else:
            break