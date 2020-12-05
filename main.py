import random


def valid_coin_flip(user_input):
    if user_input.lower() != "heads" and user_input.lower() != "tails":
        return False
    return True


def flip_coin(name1, name2):
    valid_input = False
    coin = random.randint(1, 2)
    if random.randint(1, 2) == 1:
        user_input = input(name1 + " choose heads or tails: ")
    else:
        user_input = input(name2 + " choose heads or tails: ")
    while not valid_input:
        if user_input.lower() != "heads" and user_input.lower() != "tails":
            user_input = input("invalid input, try again. heads or tails: ")
        else: valid_input = True
        # heads = 1, tails = 2
    if coin == 1 and user_input == "heads":
        return True
    return False


def start():
    p1 = input("Player 1 name: ")
    p2 = input("Player 2 name: ")
    flip_coin(p1, p2)



def create_board():
    print("Each -- is an empty 'box'. Each box corresponds to a number, starting at 1 in the top left box, then going\
     from left to right. ")
    print("__________")
    for i in range(3):
        print("|--|--|--|")
    print("----------\n")
    # print("--------")
    # for i in range(3):
    #     print("--|--|--")
    # print("--------")

start()
create_board()

# go = True
#
# def play():
#     while go:
#
# def
