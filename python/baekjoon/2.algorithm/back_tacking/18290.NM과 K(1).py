import sys


def solve(cnt, sums, si):
    global n, m, k, valid, board, ans

    if cnt == k:
        ans = max(ans, sums)
        return

    for i in range(si, n*m):
        if valid[i] > 0:
            continue

        mark(i)
        solve(cnt+1, sums + board[i], i+1)
        mark(i, un_mark=True)


def mark(i, un_mark=False):
    global valid, n, m

    marking = 1
    if un_mark:
        marking = -1

    if valid_range(i-1) and same_row(i, i-1):
        valid[i-1] += marking

    if valid_range(i+1) and same_row(i, i+1):
        valid[i+1] += marking

    if valid_range(i-m):
        valid[i-m] += marking

    if valid_range(i+m):
        valid[i+m] += marking


def valid_range(i):
    global n, m

    return 0 <= i < n*m


def same_row(i, j):
    global m

    return i//m == j//m


n, m, k = map(int, sys.stdin.readline().strip().split(" "))
board = []
for _ in range(n):
    board.extend(list(map(int, sys.stdin.readline().strip().split(' '))))

valid = [0 for _ in range(n*m)]

ans = -sys.maxsize
solve(0, 0, 0)
print(ans)