import sys
from collections import deque


def solve():
    global board, n, k, l, ms, ds

    direction = 0

    ans = 0
    body = deque([(0, 0)])
    # 이동을 하나씩 꺼내며 진행
    while ms:
        sec, nd = ms.popleft()

        # 시간초 증가
        while ans < int(sec):
            ans += 1
            is_end = move(direction, body)

            if is_end:
                return print(ans)

        # 우측으로 고개 돌림
        if nd == 'D':
            direction = (direction+1)%4
        else:
            direction = (direction-1)%4

    # 끝나지 않았으면, 남은 방향으로 계속 이동하면서 초를 증가 시킴
    while True:
        ans += 1
        is_end = move(direction, body)

        if is_end:
            return print(ans)


# 끝나면 True, 이동 가능하면 False 반환
def move(direction, body):
    global n, board, ds

    hx, hy = body[0][0], body[0][1]
    nx, ny = hx + ds[direction][0], hy + ds[direction][1]

    # 벽에 닿음
    if 0 > nx or nx >= n or 0 > ny or ny >= n:
        return True

    # 몸에 닿음
    if (nx, ny) in body:
        return True

    body.appendleft((nx, ny))
    # 사과가 없으면 꼬리 다음으로 이동
    if board[nx][ny] == 0:
        body.pop()
    else:
        # 사과 먹어 치움
        board[nx][ny] = 0

    # 이동 가능
    return False


# L          R
# 우, 하, 좌, 상
ds = [(0, 1), (1, 0), (0, -1), (-1, 0)]
n = int(sys.stdin.readline().strip())
k = int(sys.stdin.readline().strip())
# 0: 일반, 1: 사과
board = [[0 for _ in range(n)] for _ in range(n)]
for _ in range(k):
    x, y = map(int, sys.stdin.readline().strip().split(" "))
    board[x-1][y-1] = 1

l = int(sys.stdin.readline().strip())
ms = deque()
for _ in range(l):
    ms.append(tuple(sys.stdin.readline().strip().split(" ")))

solve()


# 6
# 3
# 3 4
# 2 5
# 5 3
# 3
# 3 D
# 15 L
# 17 D
