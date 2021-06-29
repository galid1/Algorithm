import sys
from collections import deque

def solve(points):
    global board, enimes, ans, n, m, dx, dy

    # points 1로 변경
    for x, y in points:
        board[x][y] = 1

    res = 0
    visited = [[False for _ in range(m)] for _ in range(n)]
    for si, sj, cnt in enimes:
        q = deque()
        q.append((si, sj))
        visited[si][sj] = True
        surrounded = True

        while q:
            ci, cj = q.popleft()
            for k in range(4):
                ni, nj = ci+dx[k], cj+dy[k]

                if 0 <= ni < n and 0 <= nj < m:
                    if board[ni][nj] == 2 and not visited[ni][nj]:
                        q.append((ni, nj))
                        visited[ni][nj] = True
                    elif board[ni][nj] == 0:
                        surrounded = False
                        break

            if not surrounded:
                break

        if surrounded:
            res += cnt

    # points 0으로 다시 변경
    for x, y in points:
        board[x][y] = 0

    # 정답 최신화
    ans = max(ans, res)


def select_two(points, i, j):
    global n, m, board

    if len(points) == 2:
        solve(points)
        return

    ni, nj = i, j
    while ni < n:
        b_ni, b_nj = ni, nj
        if nj + 1 == m:
            ni, nj = ni+1, 0
        else:
            nj += 1

        if board[b_ni][b_nj] == 0:
            points.append((b_ni, b_nj))
            select_two(points, ni, nj)
            points.pop()


# 그래프 4방향 탐색
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

# 입력
n, m = map(int, sys.stdin.readline().strip().split(" "))
board = []
for i in range(n):
    board.append(list(map(int, sys.stdin.readline().strip().split(" "))))

# 상대편 돌 그룹 위치 파악
enimes = []
visited = [[False for _ in range(m)] for _ in range(n)]
for i in range(n):
    for j in range(m):
        if board[i][j] == 2 and not visited[i][j]:
            cnt = 1
            q = deque()
            q.append((i, j))
            visited[i][j] = True

            while q:
                cx, cy = q.popleft()
                for k in range(4):
                    nx, ny = cx+dx[k], cy+dy[k]

                    if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and board[nx][ny] == 2:
                        cnt += 1
                        visited[nx][ny] = True
                        q.append((nx, ny))

            enimes.append((i, j, cnt))

ans = 0
select_two([], 0, 0)
print(ans)