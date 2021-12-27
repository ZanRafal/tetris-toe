def set1(x, y):
    print("XD")


def toggle(x, y, tile=[]):
    if tile[x][y] == "X":
        tile[x][y] = "O"
    elif tile[x][y] == "O":
        tile[x][y] = "X"
