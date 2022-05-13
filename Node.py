class Node:

    def __init__(self, y: int, x: int, end=False):
        self.y = y
        self.x = x
        self.next = []
        self.end = end

    def set_next(self, next_tile):
        self.next.append(next_tile)

    def get_next(self):
        return self.next

    def set_end(self):
        self.end = True

    def get_end(self):
        return self.end

    def print_loc(self):
        print("({},{})".format(self.y, self.x))
