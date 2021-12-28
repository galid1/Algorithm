import sys


def solve():
    global n, e, es, v1, v2

    for line in es:
        print(line)


INF = 1001
n, e = map(int, sys.stdin.readline().strip().split(" "))
es = [[INF if i != j else 0 for i in range(n)] for j in range(n)]

for _ in range(e):
    a, b, c = map(int, sys.stdin.readline().strip().split(" "))
    a, b = a-1, b-1
    es[a][b] = min(es[a][b], c)
    es[b][a] = min(es[b][a], c)

v1, v2 = map(int, sys.stdin.readline().strip().split(" "))

solve()