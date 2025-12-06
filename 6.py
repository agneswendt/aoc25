from aocd.models import Puzzle
import re 

day, year = 6, 2025

def get_input():
    data = Puzzle(year, day).input_data
    return data.splitlines()

data = get_input()

def part1():
    nums = [re.findall(r'[0-9]+', line) for line in data[:-1]]
    ops = re.findall(r'[\+|\*]+', data[-1])
    return sum(eval(op.join(line)) for op, line in zip(ops, zip(*nums)))

def part2():
    transposed = list(zip(*data[:-1]))
    groups, g = [], []

    for elem in transposed:
        elem = tuple(filter(lambda x: x != ' ', elem))
        if len(elem) == 0:
            groups.append(g)
            g = []
        else: g.append("".join(elem))
    groups.append(g)
    ops = re.findall(r'[\+|\*]+', data[-1])
    return sum(eval(op.join(g)) for op, g in zip(ops, groups))

print(part1(), part2())
