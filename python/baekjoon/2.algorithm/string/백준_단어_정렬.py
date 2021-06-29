import sys


def solve():
    global n, ss

    ss.sort()
    ss.sort(key = lambda a: len(a))

    for s in ss:
        print(s)



n = int(sys.stdin.readline().strip())
ss = set()
for _ in range(n):
    ss.add(sys.stdin.readline().strip())
ss = list(ss)
solve()