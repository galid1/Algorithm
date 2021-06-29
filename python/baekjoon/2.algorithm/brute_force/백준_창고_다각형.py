import sys
from collections import deque


def solve():
    global qs

    board = [[False for _ in range(1001)] for _ in range(1001)]

    while qs:
        cx, cy = qs.popleft()

        sqs = deque([])
        mx, my = 0, 0
        find = False
        fill_area(board, cx, cx+1, cy)
        while qs:
            nx, ny = qs.popleft()

            # 더 높은 기둥이 나온 경우
            if ny >= cy:
                fill_area(board, cx, nx, cy)
                find = True
                qs.appendleft((nx, ny))
                break

            if ny >= my:
                mx, my = nx, ny

            sqs.append((nx, ny))

        # 더 높은 기둥을 찾은 경우 해당 기둥을 기준으로 다시 반복
        if find:
            continue

        # 낮은 기둥만 존재하는 경우 처리
        while sqs:
            scx, scy = sqs.popleft()

            # 낮은 기둥들중 가장 큰 기둥을 찾으면 해당 기둥까지 해당 기둥의 높이로 채움
            if scx == mx:
                sqs.appendleft((scx, scy))
                fill_area(board, cx+1, scx, scy)
                break

        if sqs:
            qs = sqs

    # 정답
    print(get_area(board))


def fill_area(board, fx, tx, h):
    for i in range(fx, tx):
        for j in range(h):
            board[i][j] = True


def get_area(board):
    area = 0

    for i in range(1001):
        for j in range(1001):
            if board[i][j]:
                area += 1

    return area


qs = []
n = int(sys.stdin.readline().strip())
for _ in range(n):
    qs.append(tuple(map(int, sys.stdin.readline().strip().split(" "))))
qs.sort(key = lambda xy: xy[0])
qs = deque(qs)
solve()