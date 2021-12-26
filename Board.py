import random as rand
from termcolor import colored

def prepareBoard():
    board = initBoard()
    displayBoard(board)

def initBoard():
    board = []
    newLine = []

    for i in range(0, 8):
        for j in range(0, 8):
            newLine.append("X")
        board.append(newLine)
        newLine = []

    #TODO: Zmienna quantity jako parametr
    board = lockTiles(8, board)
    return board

def displayBoard(table = []):
    print("|==========================================|")
    print("| X | 1 || 2 || 3 || 4 || 5 || 6 || 7 || 8 |")
    print("|---|======================================|")
    for i in range(8):
        print('| {} '.format(i + 1), end="")
        for j in range(8):
            if table[i][j] == "W":
                print("| " + colored(table[i][j], "red") + " |", end="")
            elif table[i][j] == "O":
                print("| " + colored(table[i][j], "green") + " |", end="")
            else:
                print("| " + table[i][j] + " |", end="")
        print()
        print("|---|--------------------------------------|")
    print("|==========================================|")

def pickRandomFields(quantity):
    board = []
    newLine = []
    for i in range(0, quantity):
        for j in range(2):
            newLine.append(rand.randint(0, 7))
        board.append(newLine)
        newLine = []

    return board

def lockTiles(quantity, myBoard = []):
    randomFields = pickRandomFields(quantity)

    for i in range(len(randomFields)):
        y = randomFields[i][0]
        x = randomFields[i][1]
        myBoard[x][y] = "W"

    return myBoard

prepareBoard()
