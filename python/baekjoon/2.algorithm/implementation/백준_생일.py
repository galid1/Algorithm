import sys


def solve():
    global births


n = int(sys.stdin.readline().strip())
births = {}
for _ in range(n):
    name, d, m, y = sys.stdin.readline().strip().split(" ")
    births[name] = int(y)*10000 + int(m)*100 + int(d)

min_p, min_b, max_p, max_b = '', 20110101, '', 19891231
for name, birth in births.items():
    if birth < min_b:
        min_p = name
        min_b = birth
    if birth > max_b:
        max_p = name
        max_b = birth

print(max_p)
print(min_p)