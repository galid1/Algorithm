import sys
from collections import deque

def solve():
    global n, m, cnts, links
    zeros = deque()

    # 0인 애들 큐에 넣기
    for i in range(1, n+1):
        if cnts[i] == 0:
            zeros.append(i)

    while zeros:
        cur = zeros.popleft()
        print(cur, end=' ')

        for link in links[cur]:
            cnts[link] -= 1
            if cnts[link] == 0:
                zeros.append(link)


n, m = map(int, sys.stdin.readline().strip().split(" "))
cnts = [0 for _ in range(n+1)]
links = [[] for _ in range(n+1)]
for i in range(m):
    k, v = map(int, sys.stdin.readline().strip().split(" "))
    links[k].append(v)
    cnts[v] += 1

solve()