import sys


def solution():
    global n, board

    for i in range(n):
        for j in range(n):
            if j < n-1:
                # 오른쪽으로 바꿈
                board[i][j], board[i][j + 1] = board[i][j + 1], board[i][j]
                w_dfs(i, j)
                h_dfs(i, j)
                h_dfs(i, j+1)
                board[i][j], board[i][j + 1] = board[i][j + 1], board[i][j]
            if j == n-1:
                board[i][j], board[i][j - 1] = board[i][j - 1], board[i][j]
                h_dfs(i, j)
                board[i][j], board[i][j - 1] = board[i][j - 1], board[i][j]

            if i < n-1:
                # 아래로 바꿈
                board[i][j], board[i + 1][j] = board[i + 1][j], board[i][j]
                w_dfs(i, j)
                w_dfs(i+1, j)
                h_dfs(i, j)
                board[i][j], board[i + 1][j] = board[i + 1][j], board[i][j]
            if i == n-1:
                board[i][j], board[i - 1][j] = board[i - 1][j], board[i][j]
                w_dfs(i, j)
                board[i][j], board[i - 1][j] = board[i - 1][j], board[i][j]

    print(max_num)


def w_dfs(i, j):
    global n, board, max_num

    v = [[0 for _ in range(n)] for _ in range(n)]
    color = board[i][j]
    stack = [(i, j)]
    v[i][j] = 1
    answer = 0

    while stack:
        x, y = stack.pop()
        answer += 1

        if y+1 < n and not v[x][y+1] and color == board[x][y+1]:
            stack.append((x, y+1))
            v[x][y+1] = 1
        if y-1 >= 0 and not v[x][y-1] and color == board[x][y-1]:
            stack.append((x, y-1))
            v[x][y-1] = 1

    max_num = max(max_num, answer)


def h_dfs(i, j):
    global n, board, max_num

    v = [[0 for _ in range(n)] for _ in range(n)]
    color = board[i][j]
    stack = [(i, j)]
    v[i][j] = 1
    answer = 0

    while stack:
        x, y = stack.pop()
        answer += 1

        if x+1 < n and not v[x+1][y] and color == board[x+1][y]:
            stack.append((x+1, y))
            v[x+1][y] = 1
        if x-1 >= 0 and not v[x-1][y] and color == board[x-1][y]:
            stack.append((x-1, y))
            v[x-1][y] = 1

    max_num = max(max_num, answer)


max_num = 0
n = int(sys.stdin.readline())
board = []
for i in range(n):
    board.append(list(sys.stdin.readline().strip()))


solution()