def solution(board, aloc, bloc):
    ds = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    answer = [False, -1, -1]

    ax, ay = aloc
    bx, by = bloc
    moves = []
    dfs(ds, answer, board, ax, ay, bx, by, 0, 0, moves)

    if answer[0]:
        return answer[1]
    else:
        return answer[2]


def valid(x, y, board):
    return 0 <= x < len(board) and 0 <= y < len(board[0]) and board[x][y] == 1


def dfs(ds, answer, board, ax, ay, bx, by, turn, move, moves):
    for dx, dy in ds:
        if turn == 0:
            nx, ny = ax+dx, ay+dy
            if not valid(nx, ny, board):
                continue

            if ax == bx and ay == by:
                break

            board[ax][ay] = 0
            moves.append([turn, ax, ay, nx, ny])
            dfs(ds, answer, board, nx, ny, bx, by, 1 - turn, move + 1, moves)
            moves.pop()
            board[ax][ay] = 1

        else:
            nx, ny = bx+dx, by+dy
            if not valid(nx, ny, board):
                continue

            if ax == bx and ay == by:
                break

            board[bx][by] = 0
            moves.append([turn, bx, by, nx, ny])
            dfs(ds, answer, board, ax, ay, nx, ny, 1 - turn, move + 1, moves)
            moves.pop()
            board[bx][by] = 1


    if answer[0]:
        if turn == 1:
            answer[1] = max(answer[1], move)
    else:
        if turn == 0:
            answer[2] = max(answer[2], move)





board = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
aloc = [1, 0]
bloc = [1, 2]

# board = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
# aloc = [1, 0]
# bloc = [1, 2]

# board = [[1, 1, 1, 1, 1]]
# aloc = [0, 0]
# bloc = [0, 4]
print(solution(board, aloc, bloc))