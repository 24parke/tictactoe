import random
import math

global board
starting_player = None
other_player = None
sp_marker = None
op_marker = None
d_board = {}
d1 = {}
# global starting_player
# global other_player
# global sp_marker
# global op_marker
# global board

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


# ========================== BOARD SETTINGS (size) / USER INPUT ==========

def create_board():
    global board
    global d_board
    size = input("Size of board: ")
    size = check_input(size, 1, 9)
    board = [["--"] * int(size)] * int(size)
    print_board()

    for i in range(size):
        for a in range(size):
            d_board[a + (size * i) + 1] = i
            d1[a + (size * i) + 1] = a


def print_board():
    board_length = int(len(board))
    for i in range(board_length):
        for a in range(board_length):
            xd = a + (board_length * i) + 1
            if a == board_length - 1:
                if xd >= 10:
                    print(f'|{xd}|\n', end="")
                else:
                    print(f'|0{xd}|\n', end="")
            else:
                if xd >= 10:
                    print(f'|{xd}', end="")
                else:
                    print(f'|0{xd}', end="")

# ========================== PLAYER MOVES =================================


def user_move():
    global board
    end = False
    while not end:
        move = input(f'{starting_player}: ')
        move = check_input(move, 1, len(board) ** 2)
        board[d_board[move]][d1[move]] = "XX"
        print(board[d_board[move]][d1[move]])
        if check_win(d_board[move]):
            end = True
            break
        else:
            move = input(f'{other_player}: ')
            move = check_input(move, 1, len(board) ** 2)
            board[d_board[move]][d_board[move]] = "OO"
            if check_win(d_board[move]):
                end = True
                break


def check_win(move):
    global board
    spot = board[d_board[move]][d_board[move]]
    for h_counter in d_board:
        print(h_counter)
    # if spot == "XX" and :
    #     return True
    # elif board[move]:
    #     return True
    # elif board:
    #     return True
    # else:
    #     return False

# ========================== ACTUAL GAME =================================


def start():
    create_board()

    global starting_player
    global other_player

    p1 = input("Player 1 name: ")
    p2 = input("Player 2 name: ")
    starting_player = p1
    other_player = p2

    # user_move()
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





# class TicTacToe:
#     board = None
#     starting_player = None
#     other_player = None
#
#     def __init__(self, board, starting_player, other_player):
#         self.board = board
#         self.starting_player = starting_player
#         self.other_player = other_player
#
#     create_board()
#     p1 = input("Player 1 name: ")
#     p2 = input("Player 2 name: ")
#     p1 = p1 + "[XX]"
#     p2 = p2 + "[OO]"
#     flip_coin(p1, p2)
#     user_move()


    # def check_win(self, move):
    #     horizontal = []
    #     vertical = []
    #     diagonal = []
    #     for h_counter in range(len(TicTacToe.board)):
    #         horizontal.append(TicTacToe.board[move + h_counter])
    #         for v_counter in range(len(TicTacToe.board)):
    #             vertical.append(TicTacToe.board[move][move + v_counter])
    #             diagonal.append(TicTacToe.board[move + h_counter][move + v_counter])
    #     if TicTacToe.board[move] == "XX":
    #         return True
    #     elif TicTacToe.board[move]:
    #         return True
    #     elif TicTacToe.board:
    #         return True
    #     else:
    #         return False


# def user_move():
#     end = False
#     while not end:
#         move = input(f'{starting_player}: ')
#         check_input(move, 1, len(board) ** 2)
#         board[move][move] = "XX"
#         if check_win(move):
#             end = True
#             break
#         else:
#             move = input(f'{other_player}: ')
#             check_input(move, 1, len(board) ** 2)
#             TicTacToe.board[move][move] = "OO"