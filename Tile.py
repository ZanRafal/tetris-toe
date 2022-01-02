class Tile:

    def __init__(self, x, y, is_immutable, attribute):
        self.x = x
        self.y = y
        self.isMutable = is_immutable
        self.attribute = attribute


def toggle(self):
    if self.is_immutable:
        return

    if self.attribute == "X":
        self.attribute = "O"
    elif self.attribute == "O":
        self.attribute = "X"
