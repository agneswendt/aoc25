from aocd.models import Puzzle

day, year = 5, 2025

def get_input():
    data = Puzzle(year, day).input_data
    ranges, nums = [], []
    switch = False
    for line in data.splitlines():
        if not line:
            switch = True
        elif not switch:
            ranges.append(tuple(map(int, line.split('-'))))
        elif switch:
            nums.append(int(line))
    return ranges, nums

ranges, nums = get_input()

p1 = 0

for num in nums:
    for a, b in ranges:
        if num in range(a, b+1):
            p1 += 1
            break

ranges = sorted(ranges, key=lambda x: x[0])
flat_spans = [ranges[0]]

for s, e in ranges[1:]:
    l_s, l_e = flat_spans[-1]
    if s <= l_e:
        flat_spans[-1] = (l_s, (max(l_e, e)))
    else:
        flat_spans.append((s, e))

p2 = sum(b+1-a for a, b in flat_spans)

print(p1, p2)

    
