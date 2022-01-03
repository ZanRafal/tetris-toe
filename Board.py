import random as rand
from termcolor import colored
import os
import Shapes


def test_board():
    board = init_board(8)
    display_board(board)

def update_display(row, col, new_figure, my_board):
    Shapes.choose_from_set(row, col, new_figure, my_board)
    display_board(my_board)
    Shapes.choose_from_set(row, col, new_figure, my_board)


def display_board(table):
    os.system('clear')
    print("|==========================================|")
    print("| X | 1 || 2 || 3 || 4 || 5 || 6 || 7 || 8 |")
    print("|---|======================================|")
    for j in range(8):
        print('| {} '.format(j + 1), end="")
        for i in range(8):
            if table[i][j] == "Θ":
                print("| " + colored(table[i][j], "red") + " |", end="")
            elif table[i][j] == "O":
                print("| " + colored(table[i][j], "green") + " |", end="")
            else:
                print("| " + table[i][j] + " |", end="")
        print()
        print("|---|--------------------------------------|")
    print("|==========================================|")


def display_board2(table):
    buffer = '|=='
    for i in range(len(table)):
        buffer += '====='
    buffer += '|\n'

    buffer += '| X '
    for i in range(len(table)):
        buffer += '| ' + str(i + 1) + ' |'

    buffer += '\n|---|'
    for i in range(len(table)):
        buffer += '----'
    buffer += '------|\n'

    for j in range(8):
        buffer += '| {} '.format(j + 1)
        for i in range(8):
            if table[i][j] == "Θ":
                buffer += "| " + colored(table[i][j], "red") + " |"
            elif table[i][j] == "O":
                buffer += "| " + colored(table[i][j], "green") + " |"
            else:
                buffer += "| " + table[i][j] + " |"
        buffer += '\n|---|'
        for i in range(len(table)):
            buffer += '----'
        buffer += '------|\n'

    buffer += '|=='
    for i in range(len(table)):
        buffer += '====='
    buffer += '|'
    print(buffer)

def init_board(quantity):
    board = []
    new_line = []

    for i in range(0, 8):
        for j in range(0, 8):
            new_line.append("X")
        board.append(new_line)
        new_line = []

    board = lock_tiles(quantity, board)
    return board


def lock_tiles(quantity, my_board):
    random_fields = pick_random_fields(quantity)
    for i in range(len(random_fields)):
        x = random_fields[i][0]
        y = random_fields[i][1]
        my_board[x][y] = "Θ"

    return my_board


def pick_random_fields(quantity):
    board = []
    new_line = []
    for i in range(0, quantity):
        for j in range(2):
            new_line.append(rand.randint(0, 7))
        board.append(new_line)
        new_line = []

    return board


def number_of_x(board):
    counter = 0
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == "X":
                counter += 1
    return counter

test_board()