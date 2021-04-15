# import sys
#
# def solution(rows, columns, queries):
#     answer = []
#
#     board = [[j + columns*i for j in range(1, columns+1)] for i in range(rows)]
#
#     for q in queries:
#         answer.append(turn(board, q[0], q[1], q[2], q[3]))
#     return answer
#
#
# def turn(board, i1, j1, i2, j2):
#     i1, j1, i2, j2 = i1-1, j1-1, i2-1, j2-1
#
#     min_num = sys.maxsize
#
#     # 맨 윗줄 이동
#     rt = board[i1][j2]
#     for i in range(j2, i1, -1):
#         min_num = min(min_num, board[i1][i-1])
#         board[i1][i] = board[i1][i-1]
#
#     # 오른 쪽 줄 이동
#     rb = board[i2][j2]
#     for i in range(i2, i1+1, -1):
#         min_num = min(min_num, board[i-1][j2])
#         board[i][j2] = board[i-1][j2]
#     board[i1+1][j2] = rt
#
#     # 아랫줄 이동
#     lb = board[i2][j1]
#     for i in range(j1, j2):
#         min_num = min(min_num, board[i2][i+1])
#         board[i2][i] = board[i2][i+1]
#     board[i2][j2-1] = rb
#
#     # 왼쪽
#     for i in range(i1, i2):
#         min_num = min(min_num, 1)
#         board[i][j1] = board[i+1][j1]
#     board[i2-1][j1] = lb
#
#     min_num = min(min_num, rt, rb, lb)
#     return min_num
#
#
# solution(6, 6 , [[2,2,5,4],[3,3,6,6],[5,1,6,3]]	)
# # solution(100, 97, [[1,1,100,97]])

import sys

def solve():
    global n, m, qs
    ans = []
    board = [[i+1 + j*m for i in range(m)] for j in range(n)]

    for i1, j1, i2, j2 in qs:
        lt = board[i1][j1]
        min_num = board[i1][j1]

        for i in range(i1, i2):
            board[i][j1] = board[i+1][j1]
            min_num = min(min_num, board[i+1][j1])

        for i in range(j1, j2):
            board[i2][i] = board[i2][i+1]
            min_num = min(min_num, board[i2][i+1])

        for i in range(i2, i1, -1):
            board[i][j2] = board[i-1][j2]
            min_num = min(min_num, board[i-1][j2])

        for i in range(j2, j1, -1):
            board[i1][i] = board[i1][i-1]
            min_num = min(min_num, board[i1][i-1])

        board[i1][j1+1] = lt
        ans.append(min_num)

    # print board
    for b in board:
        print(b)

    print(ans)

n, m = map(int, sys.stdin.readline().strip().split(" "))
qs = [[0,0,2,2], [3,3,4,4]]
solve()
