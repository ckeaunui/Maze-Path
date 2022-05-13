import sys
from Node import Node
import pygame


explored_tiles = []


def get_board():
    file = 'Maze.txt'
    with open(file, 'r') as f:
        read_board = [[int(num) for num in line.split(',')] for line in f]
    return read_board


def assign_next(cur_node):
    # Is left a legal move
    try:
        if board[cur_node.y][cur_node.x - 1] == 1 and (
                cur_node.y, cur_node.x - 1) not in explored_tiles and cur_node.x - 1 >= 0:
            cur_node.set_next(Node(cur_node.y, cur_node.x - 1))
    except IndexError:
        print("Caught")

    # Is right a legal move
    try:
        if board[cur_node.y][cur_node.x + 1] == 1 and (cur_node.y, cur_node.x + 1) not in explored_tiles:
            cur_node.set_next(Node(cur_node.y, cur_node.x + 1))
    except IndexError:
        print("Caught")

    # Is up a legal move
    try:
        if board[cur_node.y - 1][cur_node.x] == 1 and (
                cur_node.y - 1, cur_node.x) not in explored_tiles and cur_node.y - 1 >= 0:
            cur_node.set_next(Node(cur_node.y - 1, cur_node.x))
    except IndexError:
        print("Caught")

    # Is down a legal move
    try:
        if board[cur_node.y + 1][cur_node.x] == 1 and (cur_node.y + 1, cur_node.x) not in explored_tiles:
            if cur_node.y + 1 == len(board) - 1:
                end_node = (Node(cur_node.y + 1, cur_node.x, True))
                cur_node.set_next(end_node)
            else:
                cur_node.set_next(Node(cur_node.y + 1, cur_node.x))
    except IndexError:
        print("Caught")

    explored_tiles.append((cur_node.y, cur_node.x))


def search(cur_node: Node):

    # If this node is the exit, print a completion message and return this tiles position
    if cur_node.get_end():
        #print("Exit: ({},{})".format(cur_node.y, cur_node.x))
        return [[cur_node.y, cur_node.x]]

    # If this node is not the exit, search its children.  Recursively do this until
    # a dead end or the exit is reached
    else:
        # assign this node its children
        assign_next(cur_node)
        children = cur_node.get_next()

        # Search each child
        for index, child in enumerate(children):

            child_res = search(child)
            if child_res:
                return [[cur_node.y, cur_node.x]] + child_res

        # Dead end
        return None


# print the board
def show_board(board):

    w_1 = screen_width / len(board[0])
    w_2 = screen_height / len(board)

    if w_1 > w_2:
        w = w_2
    else:
        w = w_1

    tile = pygame.Surface([w, w])
    maze = pygame.display.set_mode((w * len(board[0]), w * len(board)))
    border = pygame.Surface([w - 2, w - 2])

    for row in range(len(board)):
        for col in range(len(board[0])):

            if board[row][col] == 1:
                if [row, col] in final_route:
                    border.fill((100, 0, 0))
                    tile.blit(border, (1,1))

                else:
                    border.fill((100, 100, 100))
                    tile.blit(border, (1, 1))
            else:
                tile.fill((0, 0, 0))
            maze.blit(tile, (col * w, row * w))

    screen.blit(maze, (0, 0))
    pygame.display.flip()


# Get the board data from Maze.txt and return it as a 2d array of coordinates [[y, x]] starting at (0,0) top left
board = get_board()
for cur_tile in board[0]:

    if cur_tile == 1:
        start_node = Node(0, cur_tile)
        final_route = search(start_node)
        break

# Create the maze display and show it along with the solution
screen_width = 1200
screen_height = 750
screen = pygame.display.set_mode((screen_width, screen_height))
screen.fill((100,100,100))
pygame.init()
show_board(board)

# Keep the display up until the user closes it
show = True
while show:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
