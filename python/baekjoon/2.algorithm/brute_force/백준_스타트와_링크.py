from itertools import combinations
from collections import deque
import sys


def solution():
    global n, ability, ans

    team_c = deque(combinations([i for i in range(n)], n//2))

    while team_c:
        start = list(team_c.popleft())
        link = list(team_c.pop())

        start_total = 0
        link_total = 0
        for i in range(n//2 - 1):
            for j in range(i+1, n//2):
                start_total += ability[start[i]][start[j]] + ability[start[j]][start[i]]
                link_total += ability[link[i]][link[j]] + ability[link[j]][link[i]]

        ans = min(ans, abs(start_total - link_total))


n = int(sys.stdin.readline())
ability = []
for i in range(n):
    ability.append(list(map(int, sys.stdin.readline().split(" "))))
ans = sys.maxsize
solution()
print(ans)