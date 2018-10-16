import numpy as np

def merge(lst):
    moved = False
    limit = -1
    for i in range(1, len(lst)):
        if lst[i] == 0:
            continue
        else:
            curr = lst[i]
            lst[i] = 0
            new = i
            for j in range(i - 1, limit, -1):
                if lst[j] == 0:
                    moved = True
                    new = j
                elif lst[j] == curr:
                    moved = True
                    lst[j] = 2 * curr
                    curr = 0
                    limit = j
                    break
                else:
                    break

            lst[new] = curr

    return lst

class gameGenerator():
    def __init__(self, size):
        self.field = np.zeros((size, size))
        self.size = size

    def generateBlock(self):
        randRow = np.random.randint(0, 4)
        randCol = np.random.randint(0, 4)
        if self.field[randRow][randCol] == 0:
            if np.random.rand() < 0.75:
                self.field[randRow][randCol] = 2
            else:
                self.field[randRow][randCol] = 4
        else:
            self.generateBlock()

    def swipe(self, direction):
        if direction == "left":
            for i in range(self.size):
                lst = merge(self.field[i])
                self.field[i] = lst

        elif direction == "right":
            for i in range(self.size):
                lst = merge(self.field[i][::-1])
                self.field[i] = lst[::-1]

        elif direction == "up":
            for j in range(self.size):
                lst = merge(self.field[:, j])
                self.field[:, j] = lst

        elif direction == "down":
            for j in range(self.size):
                lst = merge(self.field[::-1, j])
                self.field[::-1, j] = lst
        else:
            print(" Invalid direction!")

    def print(self):
        print(self.field)

game = gameGenerator(4)

while True:
    game.generateBlock()
    game.print()

    key = input()
    if key == "j":
        game.swipe("left")
    elif key == "l":
        game.swipe("right")
    elif key == "i":
        game.swipe("up")
    elif key == "k":
        game.swipe("down")

