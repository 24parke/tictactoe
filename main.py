import random
import math


# board = None
# starting_player = None
# other_player = None
# sp_marker = None
# op_marker = None
global board
global starting_player
global other_player
global sp_marker
global op_marker

# ========================== HELPER FUNCTIONS ============================


def check_input(user_input, minimum, maximum):
    valid_input = False
    if str(minimum) == minimum and str(maximum) == maximum:
        while not valid_input:
            if user_input.lower() != minimum and user_input.lower() != maximum:
                user_input = input("Please choose either " + minimum + " or " + maximum + ". ")
            else:
                return str(user_input)
    elif int(minimum) == minimum and int(maximum) == maximum:
        while not valid_input:
            try:
                user_input = int(user_input)
                if user_input < minimum or user_input > maximum:
                    user_input = input(f'Please choose an integer between {minimum} and {maximum}: ')
                else:
                    return int(user_input)
            except ValueError:
                user_input = input(f'Please choose an integer between {minimum} and {maximum}: ')


def flip_coin(name1, name2):
    # valid_input = False
    global starting_player
    if random.randint(1, 2) == 1: coin = "heads"
    else: coin = "tails"
    if random.randint(1, 2) == 1:
        user_input = input(name1 + " choose heads or tails: ")
        user = name1
    else:
        user_input = input(name2 + " choose heads or tails: ")
        user = name2
    user_input = check_input(user_input, "heads", "tails")
    if coin == user_input:
        print("It was " + user_input + ", " + user + " goes first!")
        starting_player = user
        return user
    else:
        if user == name1:
            print("It was " + coin + ", " + name2 + " goes first!")
            starting_player = name2
            return name2
        else:
            print("It was " + coin + ", " + name1 + " goes first!")
            starting_player = name1
            return name1


# ========================== BOARD SETTINGS (size) / USER INPUT===========

def create_board():
    global board
    size = input("Size of board: ")
    size = check_input(size, 1, 9)
    board = [["--"] * int(size)] * int(size)
    print(board)
    print_board()


def print_board():
    # print("__________")
    # global board
    for i in range(int(len(board))):
        for a in range(int(len(board))):
            # make the top and bottom borders on the grid using ---------------
            # if a == 0:
            #
            if a == int(len(board)) - 1:
                if (a + 1) * (i + 1) >= 10:
                    print(f'|{(a + 1) * (i + 1)}|\n', end="")
                else:
                    print(f'|0{(a + 1) * (i + 1)}|\n', end="")
            else:
                if (a + 1) * (i + 1) >= 10:
                    print(f'|{(a + 1) * (i + 1)}', end="")
                else:
                    print(f'|0{(a + 1) * (i + 1)}', end="")
    # print("----------\n")


# ========================== ACTUAL GAME =================================


def start():
    create_board()
    global sp_marker
    global op_marker
    p1 = input("Player 1 name: ")
    p2 = input("Player 2 name: ")
    sp_marker = "XX"
    op_marker = "OO"
    user_move()


# def user_move():
#     global board
#     global starting_player
#     global other_player
#     end = False
#     while not end:
#         move = input(f'{starting_player}: ')
#         check_input(move, 1, len(board) ** 2)


start()


class TicTacToe:
    board = None
    starting_player = None
    other_player = None
    def __init__(self, board, starting_player, other_player):
        self.board = board
        self.starting_player = starting_player
        self.other_player = other_player


    create_board()
    p1 = input("Player 1 name: ")
    p2 = input("Player 2 name: ")
    flip_coin(p1, p2)

    def check_win(self, move):
        horizontal = []
        vertical = []
        diagonal = []
        for h_counter in range(len(TicTacToe.board)):
            horizontal.append(TicTacToe.board[move + h_counter])
            for v_counter in range(len(TicTacToe.board)):
                vertical.append(TicTacToe.board[move][move + v_counter])
                diagonal.append(TicTacToe.board[move + h_counter][move + v_counter])
        if TicTacToe.board[move] == "XX":
            return True
        elif TicTacToe.board[move]:
            return True
        elif TicTacToe.board:
            return True
        else:
            return False


    def user_move(self):
        end = False
        while not end:
            move = input(f'{starting_player}: ')
            check_input(move, 1, len(board) ** 2)
            board[move][move] = "XX"
            if check_win(move):
                end = True
                break
            else:
                move = input(f'{other_player}: ')
                check_input(move, 1, len(board) ** 2)
                TicTacToe.board[move][move] = "OO"