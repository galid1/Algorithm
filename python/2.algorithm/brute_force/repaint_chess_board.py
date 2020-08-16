# 백준 1018 체스판 다시 칠하기

import sys

n, m = map(int, sys.stdin.readline().split(" "))
board = []
for i in range(n):
    board.append(list(sys.stdin.readline().strip()))



result = []
def repaint_chess_board():
    for i in range(n - 7):
        for j in range(m - 7):
            repaint(i, j)

    print(min(result))


def repaint(row, col):
    # 시작이 B인 경우
    paint_num_when_start_b = 0

    for i in range(row, row + 8):
        for j in range(col, col + 8):
            # 행 = 짝수, 열 = 홀수 => W
            if i % 2 == 0 and j % 2 == 1:
                if board[i][j] == 'B':
                    paint_num_when_start_b += 1

            # 행 = 짝수, 열 = 짝수 => B
            if i % 2 == 0 and j % 2 == 0:
                if board[i][j] == 'W':
                    paint_num_when_start_b += 1

            # 행 = 홀수, 열 = 홀수 => B
            if i % 2 == 1 and j % 2 == 1:
                if board[i][j] == 'W':
                    paint_num_when_start_b += 1

            # 행 = 홀수, 열 = 짝수 => W
            if i % 2 == 1 and j % 2 == 0:
                if board[i][j] == 'B':
                    paint_num_when_start_b += 1

    # 시작이 W인 경우
    paint_num_when_start_w = 0
    for i in range(row, row + 8):
        for j in range(col, col + 8):
            # 행 = 짝수, 열 = 홀수 => B
            if i % 2 == 0 and j % 2 == 1:
                if board[i][j] == 'W':
                    paint_num_when_start_w += 1

            # 행 = 짝수, 열 = 짝수 => W
            if i % 2 == 0 and j % 2 == 0:
                if board[i][j] == 'B':
                    paint_num_when_start_w += 1

            # 행 = 홀수, 열 = 홀수 => W
            if i % 2 == 1 and j % 2 == 1:
                if board[i][j] == 'B':
                    paint_num_when_start_w += 1

            # 행 = 홀수, 열 = 짝수 => B
            if i % 2 == 1 and j % 2 == 0:
                if board[i][j] == 'W':
                    paint_num_when_start_w += 1

    result.append(min(paint_num_when_start_b, paint_num_when_start_w))


repaint_chess_board()