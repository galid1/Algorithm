import sys
from collections import deque


def solve():
    global n, m, board

    ans = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] == 1:
                continue

            ans = max(ans, bfs(i, j))

    print(ans)


def bfs(i, j):
    global ds, n, m, board, ans

    q = deque([[i, j]])
    distance = 0

    visited = [[False for _ in range(m)] for _ in range(n)]
    visited[i][j] = True

    while q:
        distance += 1

        for _ in range(len(q)):
            cx, cy = q.popleft()

            for dx, dy in ds:
                nx, ny = cx+dx, cy+dy

                if not valid(nx, ny):
                    continue

                if board[nx][ny] == 1:
                    return distance

                if visited[nx][ny]:
                    continue

                visited[nx][ny] = True
                q.append([nx, ny])


def valid(x, y):
    global n, m
    return 0 <= x < n and 0 <= y < m


ds = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]
n, m = map(int, sys.stdin.readline().strip().split(" "))
board = []
for _ in range(n):
    board.append(list(map(int, sys.stdin.readline().strip().split(" "))))

solve()