import random


def get_shape():
    return random.randint(1, 5)


def choose_game_mode(x, y, choice, tile, diffculty):
    if diffculty == 1:
        choose_from_easy_set(x, y, choice, tile)
    elif diffculty == 2:
        choose_from_easy_set(x, y, choice, tile)
    elif diffculty == 3:
        choose_from_hard_set(x, y, choice, tile)

def choose_from_hard_set(x, y, choice, tile):
    if choice == 1:
        diamond_shape(x, y, tile)
    elif choice == 2:
        cornerless_square(x, y, tile)
    elif choice == 3:
        h_shape(x, y, tile)
    elif choice == 4:
        left_diagonal_shape(x, y, tile)
    elif choice == 5:
        right_diagonal_shape(x, y, tile)

def choose_from_medium_set(x, y, choice, tile):
    if choice == 1:
        large_horizontal_rectangle_shape(x, y, tile)
    elif choice == 2:
        large_vertical_rectangle_shape(x, y, tile)
    elif choice == 3:
        small_square_shape(x, y, tile)
    elif choice == 4:
        large_square_shape(x, y, tile)
    elif choice == 5:
        t_shape(x, y, tile)


def choose_from_easy_set(x, y, choice, tile):
    if choice == 1:
        small_vertical_rectangle_shape(x, y, tile)
    elif choice == 2:
        small_horizontal_rectangle_shape(x, y, tile)
    elif choice == 3:
        center_only_shape(x, y, tile)
    elif choice == 4:
        two_one_brick_shape(x, y, tile)
    elif choice == 5:
        one_two_brick_shape(x, y, tile)


def toggle(x, y, tile):
    if x < 0 or x > 7: return
    if y < 0 or y > 7: return

    if tile[x][y] == "X":
        tile[x][y] = "O"
    elif tile[x][y] == "O":
        tile[x][y] = "X"

##Easy Set
###################################################################################

"""
 X X X 
 X O X 
 X C X 
 X O X 
 X X X  
"""
def small_vertical_rectangle_shape(x, y, tile):
    toggle(x, y, tile)      # center
    toggle(x, y - 1, tile)  # upper center
    toggle(x, y + 1, tile)  # lower center


"""
X X X X X
X O C O X
X X X X X 
"""
def small_horizontal_rectangle_shape(x, y, tile):
    toggle(x, y, tile)      # center
    toggle(x - 1, y, tile)  # left
    toggle(x + 1, y, tile)  # right


"""
X X X 
X C X 
X X X  
"""

def center_only_shape(x, y, tile):
    toggle(x, y, tile)      # center


"""
X X X X
X O C X
X X X X  
"""
def two_one_brick_shape(x, y, tile):
    toggle(x, y, tile)      # center
    toggle(x - 1, y, tile)  # left


"""
X X X 
X O X 
X C X 
X X X  
"""
def one_two_brick_shape(x, y, tile):
    toggle(x, y, tile)      # center
    toggle(x, y - 1, tile)  # upper center

##Medium Set
###################################################################################

"""
X X X X X
X O O O X
X O C O X
X X X X X 
"""
def large_horizontal_rectangle_shape(x, y, tile):
    toggle(x, y, tile)          # lower center
    toggle(x - 1, y, tile)      # lower left
    toggle(x + 1, y, tile)      # lower right
    toggle(x, y - 1, tile)      # upper center
    toggle(x - 1, y - 1, tile)  # upper left
    toggle(x + 1, y - 1, tile)  # upper right


"""
X X X X X
X O O X X
X O C X X
X O O X X
X X X X X 
"""
def large_vertical_rectangle_shape(x, y, tile):
    toggle(x, y, tile)          # center
    toggle(x, y - 1, tile)      # upper center
    toggle(x, y + 1, tile)      # lower center
    toggle(x - 1, y, tile)      # left center
    toggle(x - 1, y + 1, tile)  # lower left
    toggle(x - 1, y - 1, tile)  # upper left




"""
X X X X
X O O X
X C O X
X X X X 
"""
def small_square_shape(x, y, tile):
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
def large_square_shape(x, y, tile):
    toggle(x, y, tile)          # center
    toggle(x - 1, y, tile)      # left
    toggle(x + 1, y, tile)      # right
    toggle(x, y - 1, tile)      # upper center
    toggle(x - 1, y - 1, tile)  # upper left
    toggle(x + 1, y - 1, tile)  # upper right
    toggle(x + 1, y + 1, tile)  # lower right
    toggle(x, y + 1, tile)      # lower center
    toggle(x - 1, y + 1, tile)  # lower left


"""
O O O 
X O X 
X C X 
"""
def t_shape(x, y, tile):
    toggle(x, y, tile)          # lower center
    toggle(x, y, tile)          # center
    toggle(x, y - 1, tile)      # upper center
    toggle(x - 1, y - 1, tile)  # upper left
    toggle(x + 1, y - 1, tile)  # upper right



##Hard Set
###################################################################################


"""
X O X 
O C O 
X O X 
"""

def diamond_shape(x, y, tile):
    toggle(x, y, tile)      # center
    toggle(x - 1, y, tile)  # left
    toggle(x + 1, y, tile)  # right
    toggle(x, y - 1, tile)  # upper center
    toggle(x, y + 1, tile)  # lower center


"""

O X O 
X C X 
O X O 
"""

def cornerless_square(x, y, tile):
    toggle(x, y, tile)          # center
    toggle(x - 1, y - 1, tile)  # upper left
    toggle(x + 1, y - 1, tile)  # upper right
    toggle(x - 1, y + 1, tile)  # lower left
    toggle(x + 1, y + 1, tile)  # lower right


"""
X X X X X 
X O X O X
X O C O X
X O X O X
X X X X X
"""

def h_shape(x, y, tile):
    toggle(x, y, tile)          # center
    toggle(x - 1, y, tile)      # left
    toggle(x + 1, y, tile)      # right
    toggle(x - 1, y - 1, tile)  # upper left
    toggle(x - 1, y + 1, tile)  # lower left
    toggle(x + 1, y - 1, tile)  # upper right
    toggle(x + 1, y + 1, tile)  # lower right


""" 
O X X
X C X 
X X O 
"""

def left_diagonal_shape(x, y, tile):
    toggle(x, y, tile)          # center
    toggle(x - 1, y - 1, tile)  # upper left
    toggle(x + 1, y + 1, tile)  # lower right


"""
X X O
X C X
O X X
"""

def right_diagonal_shape(x, y, tile):
    toggle(x, y, tile)          # center
    toggle(x - 1, y + 1, tile)  # lower left
    toggle(x + 1, y - 1, tile)  # upper right