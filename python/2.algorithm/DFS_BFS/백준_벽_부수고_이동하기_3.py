import sys
from collections import deque


def solve():
    global n, m, k, board, dx, dy
    # 부순 회수                  y                   x
    visited = [[[False for _ in range(k + 1)] for _ in range(m)] for _ in range(n)]
    q = deque([[0, 0, k, 1]])
    visited[0][0][k] = True

    ans = 0
    while q:
        ans += 1

        for _ in range(len(q)):
            cx, cy, ck, is_morning = q.popleft()
            next_weather = (is_morning + 1) % 2

            # 정답
            if cx == n - 1 and cy == m - 1:
                return print(ans)

            for i in range(4):
                nx, ny = cx + dx[i], cy + dy[i]

                if not is_boundary(nx, ny):
                    continue

                # 벽인 경우
                if is_wall(nx, ny):
                    if ck - 1 >= 0 and not visited[nx][ny][ck - 1]:
                        if is_morning == 1:
                            visited[nx][ny][ck - 1] = True
                            q.append((nx, ny, ck - 1, next_weather))
                        else:
                            q.append((cx, cy, ck, next_weather))
                    continue

                if not visited[nx][ny][ck]:
                    visited[nx][ny][ck] = True
                    q.append((nx, ny, ck, next_weather))

    print(-1)



def is_boundary(x, y):
    global n, m
    if 0 <= x < n and 0 <= y < m:
        return True
    return False


def is_wall(x, y):
    global board
    if board[x][y] == 1:
        return True
    return False


dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)
n, m, k = map(int, sys.stdin.readline().strip().split(" "))
board = []
for _ in range(n):
    board.append(list(map(int, sys.stdin.readline().strip())))
solve()
