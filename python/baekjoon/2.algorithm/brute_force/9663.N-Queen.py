import sys


def solve(cur_row, visited):
    global n, ans, board

    if cur_row == n:
        ans += 1
        return

    for col in range(n):
        if visited[col]:
            continue

        if not valid(cur_row, col):
            continue

        visited[col] = True
        board[cur_row][col] = True
        solve(cur_row + 1, visited)
        visited[col] = False
        board[cur_row][col] = False


def valid(row, col):
    global n

    tr, tc = row, col
    while tr > 0 and tc > 0:
        tr, tc = tr-1, tc-1
        if board[tr][tc]:
            return False

    tr, tc = row, col
    while tr > 0 and tc < n-1:
        tr, tc = tr-1, tc+1
        if board[tr][tc]:
            return False

    return True


n = int(sys.stdin.readline().strip())
board = [[False for _ in range(n)] for _ in range(n)]
ans = 0
solve(0, [False for _ in range(n)])
print(ans)