import random as rnd


def chooseFromSet(x, y, tile=[]):
    choice = rnd.randint(0, 4)
    if choice == 0:
            large_rectangle_shape(x, y, tile)
    elif choice == 1:
            small_rectangle_shape(x, y, tile)
    elif choice == 2:
            small_square_shape(x, y, tile)
    elif choice == 3:
            large_rectangle_shape(x, y, tile)
    elif choice == 4:
            diamond_shape(x, y, tile)


def toggle(x, y, tile=[]):
    if x < 0 | x > 8: return
    if y < 0 | y > 8: return

    if tile[x][y] == "X":
        tile[x][y] = "O"
    elif tile[x][y] == "O":
        tile[x][y] = "X"


"""
X X X X X
X O O O X
X O C O X
X X X X X 
"""


def large_rectangle_shape(x, y, tile=[]):
    toggle(x, y, tile)  # lower center
    toggle(x - 1, y, tile)  # lower left
    toggle(x + 1, y, tile)  # lower right
    toggle(x, y - 1, tile)  # upper center
    toggle(x - 1, y - 1, tile)  # upper left
    toggle(x + 1, y - 1, tile)  # upper right


"""
X X X X X
X O C O X
X X X X X 
"""


def small_rectangle_shape(x, y, tile=[]):
    toggle(x, y, tile)  # center
    toggle(x - 1, y, tile)  # left
    toggle(x + 1, y, tile)  # right


"""
X X X X
X O O X
X C O X
X X X X 
"""


def small_square_shape(x, y, tile=[]):
    toggle(x, y, tile)  # lower center
    toggle(x + 1, y, tile)  # lower right
    toggle(x, y - 1, tile)  # upper left
    toggle(x + 1, y - 1, tile)  # upper right


"""
X X X X X
X O O O X
X O C O X
X O O O X
X X X X X 
"""


def large_square_shape(x, y, tile=[]):
    toggle(x, y, tile)  # center
    toggle(x - 1, y, tile)  # left
    toggle(x + 1, y, tile)  # right
    toggle(x, y - 1, tile)  # upper center
    toggle(x - 1, y - 1, tile)  # upper left
    toggle(x + 1, y - 1, tile)  # upper right
    toggle(x + 1, y + 1, tile)  # lower right
    toggle(x, y + 1, tile)  # lower center
    toggle(x - 1, y + 1, tile)  # lower left


"""
X X X X X
X X O X X
X O C O X
X X O X X
X X X X X 
"""


def diamond_shape(x, y, tile=[]):
    toggle(x, y, tile)  # center
    toggle(x - 1, y, tile)  # left
    toggle(x + 1, y, tile)  # right
    toggle(x, y - 1, tile)  # upper center
    toggle(x, y + 1, tile)  # lower center
