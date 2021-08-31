import sys
from collections import deque


def solve():
    global board, N, M, K

    for _ in range(K):
        move()
        divide()

    print(get_total_m())


def move():
    global q, board, ds, N

    def get_next_position(x, y, s, d):
        dx, dy = ds[d]

        return [(x + dx * s) % N, (y + dy * s) % N]

    temp = []
    for _ in range(len(q)):
        x, y = q.popleft()

        for _ in range(len(board[x][y])):
            m, s, d = board[x][y].popleft()
            nx, ny = get_next_position(x, y, s, d)
            temp.append([nx, ny, m, s, d])

    for nx, ny, m, s, d in temp:
        if len(board[nx][ny]) == 0:
            q.append([nx, ny])
        board[nx][ny].append([m, s, d])


def divide():
    global N, board

    for i in range(N):
        for j in range(N):
            if len(board[i][j]) <= 1:
                continue

            tm, ts, odd, even, diff = 0, 0, False, False, False
            for idx, [m, s, d] in enumerate(board[i][j]):
                tm += m
                ts += s

                if idx == 0:
                    if d % 2 == 0:
                        even = True
                    else:
                        odd = True
                else:
                    if even and d % 2 == 1:
                        diff = True
                    elif odd and d % 2 == 0:
                        diff = True

            tm = tm // 5
            ts = ts // len(board[i][j])
            board[i][j] = deque()

            if tm == 0:
                continue

            for idx in range(4):
                d = idx*2 + 1 if diff else idx*2
                board[i][j].append([tm, ts, d])


def get_total_m():
    global board, N

    sums = 0
    for i in range(N):
        for j in range(N):
            for _ in range(len(board[i][j])):
                sums += board[i][j].popleft()[0]

    return sums


ds = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]
N, M, K = map(int, sys.stdin.readline().strip().split(" "))
board = [[deque() for _ in range(N)] for _ in range(N)]
q = deque()
for _ in range(M):
    x, y, m, s, d = list(map(int, sys.stdin.readline().strip().split(" ")))
    q.append([x - 1, y - 1])
    board[x - 1][y - 1].append([m, s, d])

solve()
