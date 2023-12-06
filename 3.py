d = {}
for y, line in enumerate(open("data/3.txt", "r").read().rstrip().split("\n")):
    for x, char in enumerate(line):
        d.setdefault(y, {})[x] = char

sum = 0
stars = {}
touched_stars = set()
touched_any = False

for y in range(len(d)):
    number = ""

    def finish_number():
        global number, sum, touched_stars, touched_any
        if number:
            if touched_any:
                sum += int(number)
            for s in touched_stars:
                stars.setdefault(s, set()).add((number, (y, x)))
        number, touched_stars, touched_any = "", set(), False

    for x in range(len(d[0])):
        if d[y][x].isdigit():
            number += d[y][x]
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    if dx == 0 and dy == 0 or x + dx < 0 or y + dy < 0 or x + dx >= len(d[0]) or y + dy >= len(d):
                        continue
                    c = d[y + dy][x + dx]
                    if c == "*":
                        touched_stars.add((x + dx, y + dy))
                    if c != "." and not c.isdigit():
                        touched_any = True
        else:
            finish_number()

    finish_number()

sum2 = 0
for s in stars.values():
    if len(s) == 2:
        sum2 += int(list(s)[0][0]) * int(list(s)[1][0])

print(sum)
print(sum2)
