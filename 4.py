from aocd.models import Puzzle
from copy import deepcopy

day, year = 4, 2025

def get_input():
    data = Puzzle(year, day).input_data

    res = []
    for line in data.splitlines():
        line = line
        res.append(list(line))
    return res

board = get_input()

def count_neighbors(x, y):
    res = 0
    for n_x in range(x-1, x+2):
        for n_y in range(y-1, y+2):
            if (n_x, n_y) == (x, y): continue
            if n_x < 0 or n_y < 0: continue
            if n_x >= len(board[0]) or n_y >= len(board): continue
            if board[n_y][n_x] == '@': res += 1
    return res

res = 0
changed = True
while changed:
    changed = False
    n_board = deepcopy(board)
    for y in range(len(board)):
        for x in range(len(board[0])):
            if board[y][x] == '@' and count_neighbors(x, y) < 4:
                res += 1
                n_board[y][x] = n_board
                changed = True
    board = n_board

print(res)