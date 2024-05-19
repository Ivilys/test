import re
from random import randint


def guess_game():
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
    game_number = generate_number(game_difficulty_int)
    player_number = get_guess_from_user()
    result = compare_results(game_number, player_number)

    if result:
        print("You won")
    else:
        print("You lost")
        print("Press 1 to start again, 0 to choose another game and 3 to end")


def generate_number(game_difficulty_int):
    secret_number = randint(1, game_difficulty_int)
    return secret_number


def compare_results(game_number, player_number):
    return game_number == player_number


def get_guess_from_user():
    user_input = int(input("Enter guessed number: "))
    return user_input
