# part 1
ans = 0
for line in open("data/1.txt").read().rstrip().split("\n"):
    ans += int(next(filter(lambda x: x.isdigit(), line)) + next(filter(lambda x: x.isdigit(), reversed(line))))
print(ans)

# part 2
digits = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}
digits.update({str(i): str(i) for i in range(1, 10)})

ans = 0
for line in open("data/1.txt").read().rstrip().split("\n"):
    m = {line.find(d): digits[d] for d in digits if line.find(d) >= 0}
    ans += int(m[min(m.keys())] + m[max(m.keys())])
print(ans)
