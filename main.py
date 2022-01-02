# Rafał Zan
# 311 214

import Board
import Shapes
from modules.getChar import *


def main():
    game_board = Board.init_board(8)
    play(game_board)


def play(my_board):
    moves_count = 0
    row = col = 4
    new_figure = Shapes.get_shape()
    Board.display_board(my_board.copy())
    while True:
        ch = get_nonblock_char(0.5)
        if ch != '':
            row, col = change_position(ch, row, col)
            if ch == '\n':
                moves_count += 1
                Shapes.choose_from_set(row, col, new_figure, my_board)
                new_figure = Shapes.get_shape()
                row = col = 4
            Board.update_display(row, col, new_figure, my_board)
            display_current_moves_count(moves_count)


def change_position(var, row, col):
    if var == 'w':
        return row % 8, (col - 1) % 8
    elif var == 'a':
        return (row - 1) % 8, col % 8
    elif var == 's':
        return row % 8, (col + 1) % 8
    elif var == 'd':
        return (row + 1) % 8, col % 8
    # elif var == '\n':
    #     return 5, 5

    return row, col


def display_current_moves_count(moves_count):
    print("Aktualna liczba ruchów: {}".format(moves_count))


if __name__ == "__main__":
    main()
