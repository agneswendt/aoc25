from aocd.models import Puzzle

day, year = 1, 2025

def get_input():
    data = Puzzle(year, day).input_data
    res = []
    for line in data.splitlines():
        d, n = line[0], line[1:]
        res.append((d, int(n)))
    return res

data = get_input()
dial = 50
res = 0

for d, n in data:
    rotations = 0
    if d == 'R':
        rotations = (dial+n) // 100
        dial = (dial + n) % 100
    else:
        if dial == 0:
            rotations = abs((dial - n)) // 100
        elif dial - n < 0:
            rotations = (abs((dial - n)) // 100) + 1
        dial = (dial - n) % 100
    if rotations == 0 and dial == 0:
        rotations += 1
    res += rotations

print(res)