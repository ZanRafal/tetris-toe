def set1(x, y):
    print("XD")

"""
X X X X X
X O O O X
X O C O X
X X X X X 
"""
def rectangle_shape(x, y, tile=[]):
    toggle(x, y, tile)              #lower center
    toggle(x - 1, y, tile)          #lower left
    toggle(x + 1, y, tile)          #lower right
    toggle(x, y - 1, tile)          #upper center
    toggle(x - 1, y - 1, tile)      #upper left
    toggle(x + 1, y - 1, tile)      #upper right

"""
X X X X
X O O X
X C O X
X X X X 
"""
def small_square_shape(x, y, tile=[]):
    toggle(x, y, tile)              #lower center
    toggle(x + 1, y, tile)          #lower right
    toggle(x, y - 1, tile)          #upper left
    toggle(x + 1, y - 1, tile)      #upper right


def toggle(x, y, tile=[]):
    if tile[x][y] == "X":
        tile[x][y] = "O"
    elif tile[x][y] == "O":
        tile[x][y] = "X"
