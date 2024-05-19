import re
from CurrencyRouletteGame import *
from GuessGame import *
from MemoryGame import *


def welcome():
    print("To begin the game please tell me your name")
    name = input()
    print("Hello " + name + " and welcome to the World of Games (WoG).\nHere you can find many cool games to play.")


def load_game():
    print("Please choose the game to play:\n" +
          "1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back\n" +
          "2. Guess Game - guess a number and see if you chose like the computer\n" +
          "3. Currency Roulette - try and guess the value of a random amount of USD in ILS\n")

    while True:
        game_number = input("Enter game number: ")
        x = re.search("[1-3]", game_number)

        if not x:
            continue

        if game_number == '1':
            memory_game()
        elif game_number == '2':
            guess_game()
        elif game_number == '3':
            currency_roulette()
        else:
            print("Please, enter a number from 1 to 3 to begin the game")


load_game()

