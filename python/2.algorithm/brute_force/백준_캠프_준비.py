import sys
from itertools import combinations

def solution():
    global n, l, r, x, a

    a.sort()
    all = []
    for length in range(2, len(a)+1):
        all += list(combinations(a, length))

    ans = 0
    for t in all:
        if l <= sum(t) <= r:
            if abs(t[-1] - t[0]) >= x:
                ans += 1

    print(ans)

n, l, r, x = map(int, sys.stdin.readline().strip().split(" "))
a = list(map(int, sys.stdin.readline().strip().split(" ")))

solution()

# 3 5 6 1
# 1 2 3