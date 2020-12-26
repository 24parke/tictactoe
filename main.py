import random

board = ["--", "--", "--"]

# ========================== HELPER FUNCTIONS ===========================

# making check_input usable for both strings and ints, replace flip coin check input with a function call to this one
# after made more flexible


def check_input(user_input, minimum, maximum):
    valid_input = False
    if str(minimum) == minimum and str(maximum) == maximum:
        while not valid_input:
            if user_input.lower() != minimum and user_input.lower() != maximum:
                user_input = input("Please choose either " + minimum + " or " + maximum + ".")
            else:
                return user_input
    elif int(minimum) == minimum and int(maximum) == maximum:
        while not valid_input:
            try:
                user_input = int(user_input)
                if user_input <= minimum or user_input >= maximum:
                    user_input = input("Please choose an integer between " + minimum + " and " + maximum)
                else:
                    return user_input
            except ValueError:
                user_input = input("Please choose an integer between " + minimum + " and " + maximum)


def flip_coin(name1, name2):
    # valid_input = False
    if random.randint(1, 2) == 1: coin = "heads"
    else: coin = "tails"
    if random.randint(1, 2) == 1:
        user_input = input(name1 + " choose heads or tails: ")
        user = name1
    else:
        user_input = input(name2 + " choose heads or tails: ")
        user = name2
    # while not valid_input:
    #     if user_input.lower() != "heads" and user_input.lower() != "tails":
    #         user_input = input("invalid input, try again. heads or tails: ")
    #     else: valid_input = True
    #     # heads = 1, tails = 2
    # if coin == user_input:
    #     print("It was " + coin + ", " + user + " goes first!")
    #     return user
    # else:
    #     if user == name1:
    #         print("It was " + coin + ", " + name2 + " goes first!")
    #         return name2
    #     else:
    #         print("It was " + coin + ", " + name1 + " goes first!")
    #         return name1

    user_input = check_input(user_input)


# ========================== ACTUAL GAME =================================
def start():
    print("Each -- is an empty 'box'. Each box corresponds to a number, starting at 1 in the top left box, then going\
 from left to right. ")
    p1 = input("Player 1 name: ")
    p2 = input("Player 2 name: ")
    flip
    create_board()
    end = False

# while not end:

# make board public, make board not constrained to 3 'boxes', instead, num of boxes based on user input


def create_board():
    # board = ["--", "--", "--"]
    print("__________")
    for i in range(len(board)):
        for i in range(len(board)):
            if i == len(board) - 1:
                print("|" + board[i] + "|" + "\n", end = "")
            else:
                print("|" + board[i], end = "")
    print("----------\n")
    # print("--------")
    # for i in range(3):
    #     print("--|--|--")
    # print("--------")


def play(starting_player, name1, name2):
    valid_input = False
    while not valid_input:
        choice = input(starting_player + ": ")
        # try:
        #     choice = int(choice)
        #     if choice <= 0 or choice >= len(board) * len(board):
        #         choice = input("Please choose an integer between 1 and 9")
        #
        # except ValueError:
        #     choice = input("Please choose an integer between 1 and 9")
        check_input(choice, 0, len(board) * len(board))

create_board()
start()


# go = True
#
# def play():
#     while go:
#
# def
