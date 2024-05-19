import re
from random import randint
import requests


def currency_roulette():
    get_exchange_rate()
    while True:
        print("Please choose the game difficulty from 1 to 5")
        game_difficulty_str = input("Enter game difficulty: ")
        x = re.search("[1-5]", game_difficulty_str)
        game_difficulty_int = int(game_difficulty_str)
        if not x:
            continue
        else:
            play(game_difficulty_int)
            break


def play(game_difficulty_int: int):
    generated_number = randint(1, 101)
    print("Try to guess how much in ILS is " + str(generated_number) + " USD")
    x, y = get_money_interval(game_difficulty_int, generated_number * get_exchange_rate())
    user_guess = get_guess_from_user()

    if x < user_guess < y:
        print("You won")
    else:
        print("You lost")
        print("Press 1 to start again, 0 to choose another game and 3 to end")


def get_money_interval(game_difficulty_int,t):
    x = t - (5 - game_difficulty_int)
    y = t + (5 - game_difficulty_int)
    return x, y


def get_guess_from_user():
    user_guess = float(input("Enter your guessed value: "))
    return user_guess


def get_exchange_rate():
    rate = requests.get('https://api.frankfurter.app/latest?from=USD&to=ILS')
    print(rate.json()["rates"]["ILS"])
    return rate.json()["rates"]["ILS"]





