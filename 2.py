from functools import reduce

rules = {
    "red": 12,
    "green": 13,
    "blue": 14,
}


def get_minset(line):
    m = {}
    for draw in line[line.find(":") + 1 :].split(";"):
        for cube in draw.split(","):
            n, color = cube.strip().split(" ")
            m[color] = max(m.get(color, 0), int(n))
    return m


ans1 = 0
ans2 = 0
for idx, line in enumerate(open("data/2.txt").read().rstrip().split("\n")):
    m = get_minset(line)
    if all(m.get(color, 0) <= limit for color, limit in rules.items()):
        ans1 += idx + 1
    ans2 += reduce(lambda x, y: x * y, (v for v in m.values()))


print(ans1)
print(ans2)
