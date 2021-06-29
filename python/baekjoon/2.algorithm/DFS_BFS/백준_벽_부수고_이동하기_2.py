import sys
from collections import deque


def solve():
    global n, m, k, board, dx, dy, visited

    ans = sys.maxsize

    # 순서대로 i, j, 부순 회수, 이동 회수
    q = deque()
    q.append((0, 0, 0, 1))
    visited[0][0][0] = True

    while q:
        for i in range(len(q)):
            cx, cy, ck, move = q.popleft()

            if cx == n-1 and cy == m-1:
                ans = min(ans, move)

            for d in range(4):
                nx, ny = cx + dx[d], cy + dy[d]
                nk = ck

                if 0 <= nx < n and 0 <= ny < m:
                    if board[nx][ny] == 1:
                        nk += 1

                if is_valid(nx, ny, nk):
                    visited[nx][ny][nk] = True
                    q.append((nx, ny, nk, move+1))

    if ans == sys.maxsize:
        print(-1)
    else:
        print(ans)


def is_valid(x, y, broke):
    global n, m, k, board, visited

    if 0 <= x < n and 0 <= y < m and broke <= k and not visited[x][y][broke]:
        return True

    return False



dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)
n, m, k = map(int, sys.stdin.readline().strip().split(" "))
visited = [[[False for _ in range(k + 1)] for _ in range(m + 1)] for _ in range(n + 1)]
board = []
for i in range(n):
    board.append(list(map(int, sys.stdin.readline().strip())))

solve()

# 6 4 1
# 0100
# 1110
# 1000
# 0000
# 0111
# 0000

# 6 4 10
# 0111
# 1111
# 1111
# 1111
# 1110
# 1110
