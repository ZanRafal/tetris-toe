# Rafał Zan
# 311 214
import os
import time
import TimerLogic as tl
import Board
import Shapes
from modules.getChar import *
import MenuLogic as ml

def main():
    print(ml.get_difficulty_level())



    # game_board = Board.init_board(8, 8)
    # play(game_board)
    # menu()


def play(my_board):
    timer = time.time()
    moves_count = 0
    row = col = 4
    new_figure = Shapes.get_shape(1)
    Board.display_board(my_board.copy())
    while Board.number_of_x(my_board) != 0:
        ch = get_nonblock_char(0.5)
        time.sleep(0.01)
        timer2 = time.time()
        if ch != '':
            row, col = change_position(ch, row, col)
            if ch == '\n':
                moves_count += 1
                Shapes.choose_from_set(row, col, new_figure, my_board)
                new_figure = Shapes.get_shape(1)
                row = col = 4
        Board.update_display(row, col, new_figure, my_board)
        display_current_moves_count(moves_count)
        display_time(int(timer2 - timer))
        tl.display_score(int(timer2 - timer), moves_count)
    display_win_message()


def change_position(var, row, col):
    if var == 'w':
        return row % 8, (col - 1) % 8
    elif var == 'a':
        return (row - 1) % 8, col % 8
    elif var == 's':
        return row % 8, (col + 1) % 8
    elif var == 'd':
        return (row + 1) % 8, col % 8

    return row, col


def display_current_moves_count(moves_count):
    print("Aktualna liczba ruchów: {}".format(moves_count))


def display_win_message():
    print("Gratulacje!! Udało Ci się ukończyć grę!")


def display_time(value):
    seconds = value % 60
    minutes = value // 60
    if seconds <= 9:
        print('Czas rozgrywki: {} : 0{}'.format(minutes, seconds))
    else:
        print('{} : {}'.format(minutes, seconds))

if __name__ == "__main__":
    main()
