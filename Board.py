import numpy as np

def prepareBoard():
    initBoard()
    displayBoard()

def initBoard():
    board = []
    newLine = []
    for i in range(0, 8):
        for j in range(0, 8):
            newLine.append("X")
        board.append(newLine)
        newLine = []

    return board

def displayBoard():
    table = initBoard()
    print("|==========================================|")
    print("| X | 1 || 2 || 3 || 4 || 5 || 6 || 7 || 8 |")
    print("|---|======================================|")
    for i in range(8):
        print('| {} '.format(i + 1), end="")
        for j in range(8):
            print('| {} |'.format(table[i][j]), end="")
        print()
        print("|---|--------------------------------------|")
    print("|==========================================|")

prepareBoard()