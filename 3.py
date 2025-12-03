from aocd.models import Puzzle
from functools import cache

day, year = 3, 2025

def get_input():
    data = Puzzle(year, day).input_data

    res = []
    for line in data.splitlines():
        line = line
        res.append(line)
    return res


data = get_input()

@cache
def search(num, depth = 11):
    if len(num) == 0 or depth < 0 or depth >= len(num):
        return 0
    return max(
        search(num[1:], depth=depth),
        10**depth*num[0] + search(num[1:], depth=depth-1)
    )

p1, p2 = 0, 0
for line in data:
    line = tuple(map(int, line))
    p1 += search(line, depth=1)
    p2 += search(line, depth = 11)

print(p1, p2)






