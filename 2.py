from aocd.models import Puzzle

day, year = 2, 2025

def get_input():
    data = Puzzle(year, day).input_data
    res = []
    for line in data.splitlines():
        line = line
        res.append(line)
    res = res[0].split(',')
    n_res = []
    for line in res:
        n_res.append(tuple(line.split('-')))
    return n_res

def invalid(id: str):
    for i, _ in enumerate(id):
        for j in range(15):
            if id[:i]*j == id:
                return True
    return False

data = get_input()

p2 = 0
for a,b in data:
    a, b = int(a), int(b)
    for x in range(a, b+1):
        x_s = str(x)
        if invalid(x_s):
            p2 += int(x)

print(p2)
