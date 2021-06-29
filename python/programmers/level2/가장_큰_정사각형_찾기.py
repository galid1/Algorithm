def solution(board):
    for i in range(1, len(board)):
        for j in range(1, len(board[0])):
            if board[i][j] == 0:
                continue

            board[i][j] = min(board[i-1][j-1], board[i-1][j], board[i][j-1]) + 1

    max_row = map(max, board)
    answer = pow(max(max_row), 2)

    return answer


# solution([[0,1,1,1],
#           [1,1,1,1],
#           [1,1,1,1],
#           [0,0,1,0]])

solution([[1,1,1,0],
          [1,0,1,1],
          [1,1,1,1]])