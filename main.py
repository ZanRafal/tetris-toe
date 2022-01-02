# Rafał Zan
# 311 214

import re
import Board
import Shapes
import InputLogic as i
import keyboard as kb
from modules.getChar import *


def main():
    gameBoard = Board.initBoard()
    play(gameBoard)
    

def play(my_board = []):
    x = y = 5
    while(True):
        ch = get_nonblock_char(0.5)
        if ch != '':
            x,y = get_input_char(ch, x, y)
            print(x,y)        
 

# def play(board=None):
#     if board is None:
#         board = []

#     moves_count = 0
#     while Board.numberOfOs(board) != 0:
#         Board.displayBoard(board)
#         display_current_moves_count(moves_count)
#         pick_field(board)
#         moves_count += 1

def get_input_char(var, x, y):
    if var == 'w':
        return x, y - 1
    elif var == 'a':
        return x - 1, y
    elif var == 's':
        return x , y + 1
    elif var == 'd':
        return x + 1, y
    elif var == 'enter':
        return 5,5           

def display_current_moves_count(moves_count):
    print("Aktualna liczba ruchów: {}".format(moves_count))


def pick_field(board=None):
    if board is None:
        board = []
    x = y = 5
    get_keyboard_input(board)

    # x = int(input('Podaj numer wiersza: '))
    # y = int(input('Podaj numer kolumny: '))

    Shapes.choose_from_set(x - 1, y - 1, board)


def get_keyboard_input(table=[]):
    Board.displayBoard(table)

    hook_on_press_w = kb.on_press_key('w', lambda e: print(e.name), True)
    hook_on_press_a = kb.on_press_key('a', lambda e: print(e.name), True)
    hook_on_press_s = kb.on_press_key('s', lambda e: print(e.name), True)
    hook_on_press_d = kb.on_press_key('d', lambda e: print(e.name), True)
    hook_on_press_enter = kb.on_press_key('enter', lambda e: exit, True)
    kb.wait('enter')
    kb.unhook_all()

if __name__ == "__main__":
    main()
