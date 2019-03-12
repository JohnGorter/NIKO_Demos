# Spel raad het getal

from guessnumber import *

@log("INFO")
def main():
    game = GuessNumber(use_hints=True, numberofnumbers = 3)
    game.showName()
    game.start()

main()