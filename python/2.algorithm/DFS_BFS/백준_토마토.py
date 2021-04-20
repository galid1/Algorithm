import sys
from collections import deque


def solve():
    global n, m, k, boards, dh, dx, dy

    days = [[[0 for _ in range(k)] for _ in range(m)] for _ in range(n)]

    # 토마토 찾고 q에 넣기
    tomatos = find_tomato()
    q = deque()
    for h, x, y in tomatos:
        q.append((h, x, y))

    ans = -1
    while q:
        ans += 1

        for _ in range(len(q)):
            ch, cx, cy = q.popleft()

            # 위, 아래 방문
            for val in dh:
                nh = ch+val
                if valid_h(nh) and boards[nh][cx][cy] == 0:
                    boards[nh][cx][cy] = 1
                    q.append((nh, cx, cy))

            # 상하좌우
            for d in range(4):
                nx, ny = cx+dx[d], cy+dy[d]
                if valid_coord(nx, ny) and boards[ch][nx][ny] == 0:
                    boards[ch][nx][ny] = 1
                    q.append((ch, nx, ny))

    if not clear():
        print(-1)
    else:
        print(ans)


def clear():
    global boards, n, m, k

    for h in range(k):
        for i in range(n):
            for j in range(m):
                if boards[h][i][j] == 0:
                    return False
    return True



def valid_h(h):
    global k

    if 0<= h < k:
        return True

    return False


def valid_coord(x, y):
    global n, m

    if 0 <= x < n and 0 <= y < m:
        return True
    return False


def find_tomato():
    global boards, n, m, k
    tomatos = []

    for h in range(k):
        for i in range(n):
            for j in range(m):
                if boards[h][i][j] == 1:
                    tomatos.append((h, i, j))

    return tomatos


dh, dx, dy = (-1, 1), (-1, 1, 0, 0), (0, 0, -1, 1)
m, n, k = map(int, sys.stdin.readline().strip().split(" "))
boards = []
for _ in range(k):
    board = []
    for _ in range(n):
        board.append(list(map(int, sys.stdin.readline().strip().split(" "))))

    boards.append(board)

solve()

