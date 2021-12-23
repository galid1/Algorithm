import sys
from collections import deque

def solve():
    global n, m, board, ds

    q = deque([(0, 0, 0)])
    visited = [[-1 for _ in range(n)] for _ in range(m)]
    visited[0][0] = 0

    while q:
        cx, cy, cnt = q.popleft()

        for dx, dy in ds:
            nx, ny = cx+dx, cy+dy

            if not valid(nx, ny):
                continue

            tcnt = cnt
            if board[nx][ny] == 1:
                tcnt += 1

            if visited[nx][ny] != -1 and visited[nx][ny] <= tcnt:
                continue

            visited[nx][ny] = tcnt
            q.append((nx, ny, tcnt))

    print(visited[m-1][n-1])

def valid(x, y):
    global n, m
    return 0 <= x < m and 0 <= y < n


ds = [[-1, 0], [1, 0], [0, -1], [0, 1]]
n, m = map(int, sys.stdin.readline().strip().split(" "))
board = []
for _ in range(m):
    board.append(list(map(int, sys.stdin.readline().strip())))

solve()