import sys


def solve():
    global n, m, board, ans

    for size in range(1, max(n, m) + 1):
        for row in range(n):
            for col in range(m):
                for dr in range(-n+1, n):
                    for dc in range(-m+1, m):
                        if size != 1 and (dr == 0 and dc == 0):
                            continue

                        value = int(dfs(1, size, row, col, dr, dc))

                        if is_square(value):
                            ans = max(ans, value)


def dfs(cur_size, size, r, c, dr, dc):
    global board

    value = board[r][c]

    if cur_size == size:
        return value

    nr, nc = r+dr, c+dc
    if not valid(nr, nc):
        return '2'

    tmp = dfs(cur_size + 1, size, nr, nc, dr, dc)

    if tmp == '2':
        return '2'

    return value + tmp


def valid(r, c):
    global n, m

    return 0 <= r < n and 0 <= c < m


def is_square(num):
    candidate = ['0', '1', '4', '9']

    if hex(num)[-1] not in candidate:
        return False

    return int(int(num ** 0.5 + 0.1) ** 2) == num


n, m = map(int, sys.stdin.readline().strip().split(" "))
board = []
for _ in range(n):
    board.append(list(list(sys.stdin.readline().strip())))

ans = -1
solve()
print(ans)


# 2 4
# 1234
# 5678
