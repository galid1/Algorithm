import sys
from collections import deque


def solve():
    global n, m, sky

    clouds = deque()
    visited = [[-1 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if sky[i][j] == 'c':
                visited[i][j] = 0
                clouds.append((i, j))

    cnt = 0
    while clouds:
        cnt += 1

        for _ in range(len(clouds)):
            cx, cy = clouds.popleft()

            nx, ny = cx, cy+1
            if ny >= m:
                continue

            if visited[nx][ny] == -1:
                visited[nx][ny] = cnt

            clouds.append((nx, ny))

    for v in visited:
        print(*v)


n, m = map(int, sys.stdin.readline().strip().split(" "))
sky = []
for _ in range(n):
    sky.append(list(sys.stdin.readline().strip()))

solve()