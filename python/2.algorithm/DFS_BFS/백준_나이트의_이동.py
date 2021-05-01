import sys
from collections import deque


def solve():
    global n, fx, fy, tx, ty

    visited = [[False for _ in range(n+1)] for _ in range(n+1)]

    q = deque([(fx, fy)])
    visited[fx][fy] = True

    ans = 0
    while q:
        for _ in range(len(q)):
            cx, cy = q.popleft()

            if (cx, cy) == (tx, ty):
                return print(ans)

            for dx, dy in ds:
                nx, ny = cx+dx, cy+dy

                # 보드판 위가 아니라면 안댐
                if not is_valid(nx, ny) or visited[nx][ny]:
                    continue

                visited[nx][ny] = True
                q.append((nx, ny))

        ans += 1

    print(ans)


def is_valid(x, y):
    global n

    if not 0 <= x < n or not 0 <= y < n:
        return False

    return True


# 이동
ds = [(-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2)]
# 입력
t = int(sys.stdin.readline().strip())
for _ in range(t):
    n = int(sys.stdin.readline().strip())
    fx, fy = map(int, sys.stdin.readline().strip().split(" "))
    tx, ty = map(int, sys.stdin.readline().strip().split(" "))
    solve()
#
# cx, cy = 0 ,0
# tx, ty = 0, 7
#
# print((cx, cy) == (tx, ty))