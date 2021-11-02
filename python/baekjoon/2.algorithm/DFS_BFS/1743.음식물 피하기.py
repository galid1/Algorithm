import sys


def solve():
    global r, c, board, ds

    visited = [[False for _ in range(c)] for _ in range(r)]

    ans = 0
    for i in range(r):
        for j in range(c):
            if visited[i][j]:
                continue

            if not board[i][j]:
                continue

            visited[i][j] = True
            stack = [[i, j]]
            cur_size = 0
            while stack:
                cx, cy = stack.pop()
                cur_size += 1

                for dx, dy in ds:
                    nx, ny = cx+dx, cy+dy
                    if not valid(nx, ny):
                        continue

                    if visited[nx][ny]:
                        continue

                    if not board[nx][ny]:
                        continue

                    visited[nx][ny] = True
                    stack.append([nx, ny])

            ans = max(ans, cur_size)

    print(ans)


def valid(x, y):
    global r, c

    return 0 <= x < r and 0 <= y < c


r, c, k = map(int, sys.stdin.readline().strip().split(' '))
board = [[False for _ in range(c)] for _ in range(r)]
for _ in range(k):
    x, y = map(int, sys.stdin.readline().strip().split(" "))
    x, y = x-1, y-1
    board[x][y] = True

ds = [[-1, 0], [1, 0], [0, -1], [0, 1]]
solve()