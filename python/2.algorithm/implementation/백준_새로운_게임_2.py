import sys
from collections import deque


def solve():
    global n, k, board, positions, stacked

    turn = 0
    while turn <= 1000:
        turn += 1

        for cur_hi in range(1, k+1):
            cx, cy, cd = positions[cur_hi]
            dx, dy = ds[cd]
            nx, ny = cx+dx, cy+dy

            # 파란칸
            if not valid(nx, ny) or board[nx][ny] == 2:
                reverse_direction = reverse(cd)
                positions[cur_hi][2] = reverse_direction

                rdx, rdy = ds[reverse_direction]
                nx, ny = cx+rdx, cy+rdy

                # 이동하려는 칸이 파란칸
                if not valid(nx, ny) or board[nx][ny] == 2:
                    continue

                if board[nx][ny] == 1:
                    do_red(cur_hi, cx, cy, nx, ny)

                elif board[nx][ny] == 0:
                    do_white(cur_hi, cx, cy, nx, ny)

            else:
                if board[nx][ny] == 1:
                    do_red(cur_hi, cx, cy, nx, ny)

                elif board[nx][ny] == 0:
                    do_white(cur_hi, cx, cy, nx, ny)

            if end(len(stacked[nx][ny])):
                return print(turn)

    return print(-1)


def do_red(cur_hi, cx, cy, nx, ny):
    global stacked

    top_hi = stacked[cx][cy][-1]
    while top_hi != cur_hi:
        positions[top_hi][0], positions[top_hi][1] = nx, ny
        stacked[nx][ny].append(stacked[cx][cy].pop())
        top_hi = stacked[cx][cy][-1]
    positions[cur_hi][0], positions[cur_hi][1] = nx, ny
    stacked[nx][ny].append(stacked[cx][cy].pop())


def do_white(cur_hi, cx, cy, nx, ny):
    global stacked

    new_stack = deque()
    top_hi = stacked[cx][cy][-1]
    while top_hi != cur_hi:
        positions[top_hi][0], positions[top_hi][1] = nx, ny
        new_stack.appendleft(stacked[cx][cy].pop())
        top_hi = stacked[cx][cy][-1]
    positions[cur_hi][0], positions[cur_hi][1] = nx, ny
    new_stack.appendleft(stacked[cx][cy].pop())

    stacked[nx][ny] = stacked[nx][ny] + new_stack


def end(stacked_len):
    return stacked_len >= 4


def reverse(direction):
    reverse_direction = (direction+1) % 2
    if direction > 1:
        reverse_direction += 2
    return reverse_direction


def valid(x, y):
    global n
    return 0 <= x < n and 0 <= y < n


ds = [[0, 1], [0, -1], [-1, 0], [1, 0]]
n, k = map(int, sys.stdin.readline().strip().split(" "))
board = []
for _ in range(n):
    board.append(list(map(int, sys.stdin.readline().strip().split(" "))))

stacked = [[deque([]) for _ in range(n)] for _ in range(n)]
positions = [[] for _ in range(k+1)]
for i in range(1, k+1):
    x, y, d = map(int, sys.stdin.readline().strip().split(" "))
    x, y, d = x-1, y-1, d-1
    positions[i] = [x, y, d]
    stacked[x][y].append(i)

solve()
