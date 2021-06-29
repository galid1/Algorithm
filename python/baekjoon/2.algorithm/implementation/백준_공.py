import sys


def solve():
    global n, switchs

    cups = [0, 1, 2, 3]

    for f, t in switchs:
        fi = cups.index(f)
        ti = cups.index(t)
        cups[fi], cups[ti] = cups[ti], cups[fi]

    print(cups[1])



n = int(sys.stdin.readline().strip())
switchs = []
for _ in range(n):
    switchs.append(list(map(int, sys.stdin.readline().strip().split(" "))))
solve()
