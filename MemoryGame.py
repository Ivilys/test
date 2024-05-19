import re
from random import randint
import time


def memory_game():
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
    game_sequence = generate_sequence(game_difficulty_int)

    print(game_sequence, end=" ")
    time.sleep(0.7)
    print("\r                 ")

    player_sequence = get_list_from_user(game_difficulty_int)

    result = is_list_equal(game_sequence, player_sequence)
    if result:
        print("You won")
    else:
        print("You lost")
        print("Press 1 to start again, 0 to choose another game and 3 to end")


def generate_sequence(game_difficulty_int):
    print("Please try to remember the sequence it will be shown for a small period of time.\n")
    input("Press any key to start.")

    game_sequence = []
    for x in range(game_difficulty_int):
        sequence = randint(1, 101)
        game_sequence.append(sequence)

    return game_sequence


def get_list_from_user(game_difficulty_int):
    player_sequence = []
    for x in range(game_difficulty_int ):
        sequence = int(input("Enter next character: "))
        player_sequence.append(sequence)

    return player_sequence


def is_list_equal(game_sequence, player_sequence):
    for x in range(len(game_sequence)):
        print(game_sequence[x], player_sequence[x])
        if game_sequence[x] != player_sequence[x]:
            return False

    return True
