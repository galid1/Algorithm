import sys
from collections import deque


def solve():
    global k, n, m, board, ds, kds, visited

    q = deque([(k, 0, 0)])
    visited[k][0][0] = True

    ans = 0
    while q:
        for _ in range(len(q)):
            ck, cx, cy = q.popleft()

            if cx == n - 1 and cy == m - 1:
                return print(ans)

            if ck >= 1:
                for kdx, kdy in kds:
                    knx, kny = cx+kdx, cy+kdy
                    nk = ck - 1

                    if not valid(knx, kny, nk):
                        continue

                    visited[nk][knx][kny] = True
                    q.append((nk, knx, kny))

            for dx, dy in ds:
                nx, ny = cx+dx, cy+dy

                if not valid(nx, ny, ck):
                    continue

                visited[ck][nx][ny] = True
                q.append((ck, nx, ny))

        ans += 1

    print(-1)


def valid(x, y, k):
    global n, m, visited, board

    return 0 <= x < n and 0 <= y < m and not visited[k][x][y] and board[x][y] != 1


ds = [[-1, 0], [1, 0], [0, -1], [0, 1]]
kds = [[-1, -2], [-2, -1], [-2, 1], [-1, 2], [1, -2], [2, -1], [2, 1], [1, 2]]
k = int(sys.stdin.readline().strip())
m, n = map(int, sys.stdin.readline().strip().split(" "))
visited = [[[False for _ in range(m)] for _ in range(n)] for _ in range(k + 1)]
board = []
for _ in range(n):
    board.append(list(map(int, sys.stdin.readline().strip().split(" "))))
solve()


# 1
# 4 4
# 0 0 0 0
# 1 0 0 0
# 0 0 1 1
# 0 1 0 1

