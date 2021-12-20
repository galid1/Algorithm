import sys


def solve():
    global n, cs

    cs.sort(key=lambda item: (item[1], item[0]))
    for c in cs:
        print(*c)


n = int(sys.stdin.readline().strip())
cs = []
for _ in range(n):
    cs.append(list(map(int, sys.stdin.readline().strip().split(" "))))

solve()