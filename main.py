import random


def valid_coin_flip(user_input):
    if user_input.lower() != "heads" and user_input.lower() != "tails":
        return False
    return True


def flip_coin(name1, name2):
    valid_input = False
    if random.randint(1, 2) == 1: coin = "heads"
    else: coin = "tails"
    if random.randint(1, 2) == 1:
        user_input = input(name1 + " choose heads or tails: ")
        user = name1
    else:
        user_input = input(name2 + " choose heads or tails: ")
        user = name2
    while not valid_input:
        if user_input.lower() != "heads" and user_input.lower() != "tails":
            user_input = input("invalid input, try again. heads or tails: ")
        else: valid_input = True
        # heads = 1, tails = 2
    if coin == user_input:
        print("It was " + coin + ", " + user + " goes first!")
        return user
    else:
        if user == name1:
            print("It was " + coin + ", " + name2 + " goes first!")
            return name2
        else:
            print("It was " + coin + ", " + name1 + " goes first!")
            return name1


def start():
    print("Each -- is an empty 'box'. Each box corresponds to a number, starting at 1 in the top left box, then going\
from left to right. ")
    p1 = input("Player 1 name: ")
    p2 = input("Player 2 name: ")
    create_board()
    end = False
    while not end:


def create_board():

    print("__________")
    for i in range(3):
        print("|--|--|--|")
    print("----------\n")
    # print("--------")
    # for i in range(3):
    #     print("--|--|--")
    # print("--------")


def play(starting_player, name1, name2):
    valid_input = False
    while not valid_input:
        choice = input(starting_player + ": ")
        if choice <= 0 or choice >= 10:



start()


# go = True
#
# def play():
#     while go:
#
# def
