import sys, copy
from collections import deque


def plant_viruses(planted, i, j):
    global m, m, maps

    if len(planted) == m:
        spread(planted, copy.deepcopy(maps))
        return

    while i < n:
        if j + 1 < n:
            j += 1
        else:
            i, j = i+1, 0

        if i < n and maps[i][j] == 2:
            planted.append([i, j])
            plant_viruses(planted, i, j)
            planted.pop()


def spread(virus_positions, maps):
    global ans, n, ds

    q = deque(virus_positions)
    visited = [[False for _ in range(n)] for _ in range(n)]

    # 방문 체크
    for x, y in q:
        visited[x][y] = True

    sec = -1
    while q:
        sec += 1

        for _ in range(len(q)):
            cx, cy = q.popleft()

            for dx, dy in ds:
                nx, ny = cx+dx, cy+dy

                if not valid(nx, ny):
                    continue

                if visited[nx][ny]:
                    continue

                visited[nx][ny] = True
                if maps[nx][ny] == 0 or maps[nx][ny] == 2:
                    q.append([nx, ny])
                    maps[nx][ny] = 2

    if all_infected(maps):
        ans = min(ans, sec)


def valid(x, y):
    global n

    return 0 <= x < n and 0 <= y < n


def all_infected(maps):
    global n

    for i in range(n):
        for j in range(n):
            if maps[i][j] == 0:
                return False

    return True


n, m = map(int, sys.stdin.readline().strip().split(" "))
maps = []
for _ in range(n):
    maps.append(list(map(int, sys.stdin.readline().strip().split(" "))))

ds = [[-1, 0], [1, 0], [0, -1], [0, 1]]
ans = sys.maxsize
plant_viruses([], 0, -1)

if ans == sys.maxsize:
    print(-1)
else:
    print(ans)