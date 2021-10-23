from collections import deque


def solution(macaron):
    EMPTY = 0
    board = [[EMPTY for _ in range(6)] for _ in range(6)]


    for col, c in macaron:
        drop(col-1, c, board)
        broken = break_m(board)

        while broken:
            pull(board)
            broken = break_m(board)

    answer = []
    for b in board:
        answer.append(''.join(list(map(str, b))))
    return answer



def pull(board):
    for col in range(6):
        b = 6
        for row in range(6-1, -1, -1):
            if board[row][col]:
                if b - 1 == row:
                    b -= 1
                    continue

                board[b-1][col] = board[row][col]
                board[row][col] = 0
                b -= 1


def break_m(board):
    ds = [[-1, 0], [1, 0], [0, -1], [0, 1]]

    visited = [[False for _ in range(6)] for _ in range(6)]

    broken = False

    for i in range(6):
        for j in range(6):
            if not board[i][j]:
                continue

            if visited[i][j]:
                continue

            visited[i][j] = True
            cur_color = board[i][j]
            linked = [[i, j]]
            q = deque([[i, j]])
            while q:
                cx, cy = q.popleft()

                for dx, dy in ds:
                    nx, ny = cx+dx, cy+dy

                    if not valid(nx, ny):
                        continue

                    if visited[nx][ny]:
                        continue

                    if board[nx][ny] != cur_color:
                        continue

                    visited[nx][ny] = True
                    q.append([nx, ny])
                    linked.append([nx, ny])

            if len(linked) >= 3:
                broken = True
                for i, j in linked:
                    board[i][j] = 0

    return broken


def valid(x, y):
    return 0 <= x < 6 and 0 <= y < 6


def drop(col, c, board):
    for row in range(6-1):
        if board[row+1][col]:
            board[row][col] = c
            return row, col

    board[5][col] = c
    return 5, col


# solution([[1,1],[2,1],[1,2],[3,3],[6,4],[3,1],[3,3],[3,3],[3,4],[2,1]])
print(solution([[1,1],[1,2],[1,4],[2,1],[2,2],[2,3],[3,4],[3,1],[3,2],[3,3],[3,4],[4,4],[4,3],[5,4],[6,1]]))