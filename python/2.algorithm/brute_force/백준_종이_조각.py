import sys

# 1. board를 재귀로 0, 1 로 체크한다. (모든 경우를 다 따져야 함)
# 2. board에 0은 가로로 연결된 경우, 1은 세로로 연결된 경우 이다.
# 3. 체크한 수가 m*n이면 재귀를 멈추고 board판의 값을 방향에 맞게 모두 더해 최대값을 갱신한다.
def check(i, j, cnt):
    global n, m, board, checked

    if cnt == n*m:
        solve()
        return

    if j+1 == m:
        i += 1
        j = 0
    else:
        j += 1

    checked[i][j] = 0
    check(i, j, cnt+1)

    checked[i][j] = 1
    check(i, j, cnt+1)


def solve():
    global n, m, board, checked, ans

    visited = [[False for _ in range(m)] for _ in range(n)]

    stack = []
    res = 0
    for i in range(n):
        for j in range(m):
            if visited[i][j]:
                continue

            visited[i][j] = True
            stack.append((i, j))
            direction = checked[i][j]
            t_res = ''

            while stack:
                cx, cy = stack.pop()
                t_res += board[cx][cy]

                nx, ny = (cx, cy+1) if direction == 0 else (cx+1, cy)

                if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and checked[nx][ny] == direction:
                    visited[nx][ny] = True
                    stack.append((nx, ny))

            res += int(t_res)

    ans = max(ans, res)


n, m = map(int, sys.stdin.readline().strip().split(" "))
board = []
for _ in range(n):
    board.append(list(sys.stdin.readline().strip()))

ans = 0
checked = [[-1 for _ in range(m)] for _ in range(n)]
a = 0
check(0, -1, 0)
print(ans)

# 4 4
# 1000
# 0001
# 0000
# 1000