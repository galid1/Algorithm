import sys
from collections import deque


def solve():
    global n, k, ds, s, tx, ty

    viruses = find_viruses()
    viruses.sort(key=lambda item: item[0])
    viruses = deque(viruses)

    cs = 0
    while viruses and cs < s:
        cs += 1

        for _ in range(len(viruses)):
            v_num, cx, cy = viruses.popleft()

            for dx, dy in ds:
                nx, ny = cx+dx, cy+dy

                if not is_valid(nx, ny):
                    continue

                viruses.append((v_num, nx, ny))
                board[nx][ny] = v_num

    print(board[tx-1][ty-1])


def find_viruses():
    global board, n

    viruses = []
    for i in range(n):
        for j in range(n):
            if board[i][j] > 0:
                viruses.append((board[i][j], i, j))

    return viruses


def is_valid(x, y):
    global board, n

    return 0 <= x < n and 0 <= y < n and board[x][y] == 0



ds = [(-1, 0), (1, 0), (0, -1), (0, 1)]
n, k = map(int, sys.stdin.readline().strip().split(" "))
board = []
for _ in range(n):
    board.append(list(map(int, sys.stdin.readline().strip().split(" "))))
s, tx, ty = map(int, sys.stdin.readline().strip().split(" "))
solve()