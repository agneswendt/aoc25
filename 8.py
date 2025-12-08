from aocd.models import Puzzle
from heapq import heappush, heappop
from functools import reduce
import math

day, year = 8, 2025

def get_input():
    data = Puzzle(year, day).input_data
    res = []
    for line in data.splitlines():
        res.append(tuple(map(int, line.split(','))))
    return res

def merge_groups(i, j, groups):
    filtered_out = [g for g in groups if (i not in g) and (j not in g)]
    filtered_in = [g for g in groups if (i in g) or (j in g)]
    new_group = reduce(lambda x, y: x|y, filtered_in+[{i, j}])
    return filtered_out + [new_group]

data = get_input()

Q = []
for i, point1 in enumerate(data):
    for j, point2 in enumerate(data[i+1:], start=i+1):
        heappush(Q, (math.dist(point1, point2), (i, j)))

iter = 0
groups = []
p1, p2 = None, None

while True:
    dist, (i, j) = heappop(Q)
    groups = merge_groups(i, j, groups)
    if iter == 1000:
        *_, a, b, c = sorted(len(g) for g in groups if g)
        p1 = a*b*c
    if len(groups[-1]) == len(data):
        p2 = data[i][0]*data[j][0]
        break
    iter += 1

print(p1, p2)
