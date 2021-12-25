import numpy as np

def prepareBoard():
    initBoard()
    displayBoard()

def initBoard():
    board = []
    newLine = []
    for i in range(0, 10):
        for j in range(0, 10):
            newLine.append("X")
        board.append(newLine)
        newLine = []

    return board

def displayBoard():
    table = initBoard()
    for i in range(10):
        for j in range(10):
            print(table[i][j], end=" ")
        print()

prepareBoard()