import sys


def solve():
    global board, calls

    bingo = 0
    cnt = 0
    for line in calls:
        for c in line:
            cnt += 1
            # c 찾기
            for i in range(5):
                for j in range(5):
                    if board[i][j] == c:
                        board[i][j] = True

            bingo += check(i, j)
            if bingo == 3:
                return print(cnt)


def check(i, j):
    global board
    line = 0

    # 중간으로 모든 대각선과 가로세로 확인
    if i == 2 and j == 2:
        # 가로
        cnt = 0
        for k in range(5):
            if board[2][k]:
                cnt += 1
        if cnt == 5:
            line += 1



        return line

    # 대각선과 가로세로 확인
    if (i == 0 and j == 0) or (i == 4 and j == 0) or (i == 0 and j == 4) or (i == 4 and j == 4):

        return line
    # 가로 세로만 확인

    return line


board = []
for _ in range(5):
    board.append(list(map(int, sys.stdin.readline().strip().split(" "))))

calls = []
for _ in range(5):
    calls.append(list(map(int, sys.stdin.readline().strip().split(" "))))
solve()