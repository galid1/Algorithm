import sys, copy


def solve(ts_ord):
    global k, visited, ans
    if len(ts_ord) == k:
        ans = min(ans, turn(ts_ord))
        return

    for i in range(k):
        if not visited[i]:
            visited[i] = True
            ts_ord.append(i)
            solve(ts_ord)
            ts_ord.pop()
            visited[i] = False


def turn(ts_ord):
    global board, ts
    tmp_board = copy.deepcopy(board)

    for idx in ts_ord:
        r, c, s = ts[idx]
        i1, j1, i2, j2 = r-s-1, c-s-1, r+s-1, c+s-1

        while (i1, j1) < (i2, j2):
            lt = tmp_board[i1][j1]

            # 왼쪽 줄
            for i in range(i1, i2):
                tmp_board[i][j1] = tmp_board[i+1][j1]

            # 아래쪽 줄
            for i in range(j1, j2):
                tmp_board[i2][i] = tmp_board[i2][i+1]

            # 오른쪽 줄
            for i in range(i2, i1, -1):
                tmp_board[i][j2] = tmp_board[i-1][j2]

            # 윗 줄
            for i in range(j2, j1, -1):
                tmp_board[i1][i] = tmp_board[i1][i-1]

            tmp_board[i1][j1+1] = lt

            # 안쪽 사각형으로
            i1, j1 = i1+1, j1+1
            i2, j2 = i2-1, j2-1

    res = sys.maxsize
    for b in tmp_board:
        res = min(res, sum(b))

    return res


n, m, k = map(int, sys.stdin.readline().strip().split(" "))
board = []
for i in range(n):
    board.append(list(map(int, sys.stdin.readline().strip().split(" "))))
ts = []
for i in range(k):
    ts.append(list(map(int, sys.stdin.readline().strip().split(" "))))

ans = sys.maxsize
visited = [False for _ in range(k)]
solve([])
print(ans)

