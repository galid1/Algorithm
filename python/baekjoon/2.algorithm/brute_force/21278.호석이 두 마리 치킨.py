import sys
from itertools import combinations

def solve(g):
    global n, m

    min_g = floid(g)
    min_v1, min_v2, min_sum = 101, 101, 100000

    for v1, v2 in combinations([i for i in range(n)], 2):
        cur_sum = 0
        for t in range(n):
            cur_sum += min(min_g[v1][t], min_g[v2][t])
        cur_sum *= 2

        if min_sum > cur_sum:
            min_v1, min_v2, min_sum = v1, v2, cur_sum
        elif min_sum == cur_sum:
            if min_v1 > v1:
                min_v1, min_v1 = v1, v2
            elif min_v1 == v1:
                if min_v2 > v2:
                    min_v2 = v2

    print(min_v1+1, min_v2+1, min_sum)


def floid(g):
    global n, INF
    min_g = [g[i].copy() for i in range(n)]


    # 거쳐 가는 점
    for via in range(n):
        for f in range(n):
            if via == f:
                continue

            for t in range(n):
                # 목적지가 출발지와 같은 경우
                if f == t:
                    continue

                # 경유지가 목적지와 같은 경우
                if t == via:
                    continue

                min_g[f][t] = min(min_g[f][t], min_g[f][via] + min_g[via][t])

    return min_g


n, m = map(int, sys.stdin.readline().strip().split(" "))

INF = 10000
g = [[INF if i != j else 0 for i in range(n)] for j in range(n)]
for _ in range(m):
    f, t = map(lambda item: int(item) - 1, sys.stdin.readline().strip().split(" "))
    g[f][t] = 1
    g[t][f] = 1

solve(g)
