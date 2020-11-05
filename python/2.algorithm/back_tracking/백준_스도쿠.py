import sys


def get_valid_list(i, j):
    global rects, board

    valid_list = [k for k in range(1, 10)]

    for h in range(9):
        # 가로
        if board[i][h] in valid_list:
            valid_list.remove(board[i][h])
        # 세로
        if board[h][j] in valid_list:
            valid_list.remove(board[h][j])

    # 사각형
    for ri in range((i//3) * 3, ((i//3) * 3) + 3):
        for rj in range((j//3)*3, ((j//3) * 3) + 3):
            if board[ri][rj] in valid_list:
                valid_list.remove(board[ri][rj])

    return valid_list


def solution(ij_idx):
    global board, zeros, printed

    if printed:
        return

    # 정답
    if ij_idx == len(zeros):
        for row in board:
            print(*row)
            printed = True
        return

    i, j = zeros[ij_idx]
    valid_list = get_valid_list(i, j)

    for vn in valid_list:
        board[i][j] = vn
        solution(ij_idx + 1)
        board[i][j] = 0


# 정답 출력 했는지
printed = False
board = []
for i in range(9):
    board.append(list(map(int, sys.stdin.readline().strip().split(" "))))

zeros = []
for i in range(9):
    for j in range(9):
        if board[i][j] == 0:
            zeros.append((i,j))

solution(0)


