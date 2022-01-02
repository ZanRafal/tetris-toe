class Tile:

    def __init__(self, x, y, isImmutable, attribute):
        self.x = x
        self.y = y
        self.isMutable = isImmutable
        self.attribute = attribute

def toggle(self):
    if self.isImmutable == True: return

    if self.attribute == "X":
        self.attribute = "O"
    elif self.attribute == "O":
        self.attribute = "X"