# Rafał Zan
# 311 214

import Board
import Shapes
from modules.get_char import *

def main():
    gameBoard = Board.initBoard()
    play(gameBoard)



def play(board=[]):
    movesCount = 0
    while Board.numberOfOs(board) != 0:
        Board.displayBoard(board)
        displayCurrentMovesCount(movesCount)
        pickField()

def displayCurrentMovesCount(movesCount):
    print("Aktualna liczba ruchów: {}".format(movesCount))

def pickField(board=[]):
    x = input("Podaj numer wiersza: ")
    y = input("Podaj numer kolumny: ")



main()