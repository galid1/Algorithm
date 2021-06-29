import sys


def solve(a, b):
    global n, t, cities, sps, d

    res = d[a][b]

    # 둘다 일반인 경우, a에서 가장 가까운 t도시로 직접 이동, 그 다음 b와 가장 가까운 t도시로 teleport로 이동 , 가장 가까운 t도시에서 b로 직접 이동
    if not sps[a] and not sps[b]:
        nearA = near_sp_from(a)
        nearB = near_sp_from(b)
        print(min(res, d[a][nearA] + t + d[b][nearB]))
        return

    # t로 가능한 경우
    if sps[a] and sps[b]:
        print(min(res, t))
        return

    # a만 sp
    if sps[a] and not sps[b]:
        nearB = near_sp_from(b)
        print(min(res, t + d[nearB][b]))
        return

    # b만 sp
    if sps[b] and not sps[a]:
        nearA = near_sp_from(a)
        print(min(res, t + d[nearA][a]))


def near_sp_from(city):
    global n, cities, sps, d

    min_idx = -1
    min_d = sys.maxsize

    for i in range(1, n+1):
        if i == city or not sps[i]:
            continue

        dist = d[city][i]
        if min_d > dist:
            min_idx = i
            min_d = dist

    return min_idx





n, t = map(int, sys.stdin.readline().strip().split(" "))
cities = [0]
sps = {i:False for i in range(1, n+1)}

for i in range(1, n+1):
    sp, x, y = map(int, sys.stdin.readline().strip().split(" "))
    cities.append((x, y, sp))
    if sp == 1:
        sps[i] = True

d = [[0 for _ in range(n+1)] for _ in range(n+1)]
for j in range(1, n):
    for k in range(j+1, n+1):
        d[j][k] = d[k][j] = abs(cities[j][0] - cities[k][0]) + abs(cities[j][1] - cities[k][1])

m = int(sys.stdin.readline().strip())
for _ in range(m):
    a, b = map(int, sys.stdin.readline().strip().split(" "))
    solve(a, b)

