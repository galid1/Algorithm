import sys
from collections import deque


def solve():
    global n, m, board, max_area, ds

    visited = [[False for _ in range(m)] for _ in range(n)]
    picture_cnt = 0

    for i in range(n):
        for j in range(m):
            if visited[i][j] or board[i][j] == 0:
                continue

            picture_cnt += 1
            q = deque([(i, j)])
            visited[i][j] = True
            area = 0
            while q:
                cx, cy = q.popleft()
                area += 1

                for dx, dy in ds:
                    nx, ny = cx+dx, cy+dy

                    if not is_valid(nx, ny, visited):
                        continue

                    if board[nx][ny] == 1:
                        visited[nx][ny] = True
                        q.append((nx, ny))

            max_area = max(max_area, area)

    print(picture_cnt)
    print(max_area)



def is_valid(x, y, visited):
    global n, m
    return 0 <= x < n and 0 <= y < m and not visited[x][y]



ds = [(-1, 0), (1, 0), (0, -1), (0, 1)]
n, m = map(int, sys.stdin.readline().strip().split(" "))
board = []
for _ in range(n):
    board.append(list(map(int, sys.stdin.readline().split(" "))))
max_area = 0
solve()