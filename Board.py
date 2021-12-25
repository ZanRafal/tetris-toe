import numpy as np

def prepareBoard():
    initBoard()

def initBoard():
    board = []
    newLine = []
    for i in range(0, 10):
        for j in range(0, 10):
            newLine.append("X")
        board.append(newLine)
        newLine = []

    return board

prepareBoard()