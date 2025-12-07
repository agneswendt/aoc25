from aocd.models import Puzzle
from functools import cache

day, year = 7, 2025

def get_input():
    data = Puzzle(year, day).input_data
    res = []
    for line in data.splitlines():
        res.append(list(line))
    return res

board = get_input()

start = None
for y in range(len(board)):
    for x in range(len(board[0])):
        if board[y][x] == 'S':
            start = (x, y)
            break

def p1(curr, visited=set()):
    x, y = curr
    while 0<=y<len(board)-1 and board[y][x] != '^': y += 1
    if (x, y) in visited: return 0
    visited.add((x, y))
    if board[y][x] == '^':
        return 1 + p1((x+1, y), visited) + p1((x-1, y), visited)
    return 0

@cache
def p2(curr):
    x, y = curr
    while 0<=y<len(board)-1 and board[y][x] != '^': y += 1
    if board[y][x] == '^':
        return p2((x+1, y)) + p2((x-1, y))
    return 1

print(p1(start), p2(start))
