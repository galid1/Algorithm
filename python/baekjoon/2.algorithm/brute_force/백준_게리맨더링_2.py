import sys


def choice_ds(x, y, d1, d2):
    global n

    if d1 > 0 and d2 > 0:
        solve(x, y, d1, d2)
        return

    # i == d1, j == d2
    for i in range(1, n):
        for j in range(1, n):
            if y - i >= 0 and y + j < n and x + i + j < n:
                choice_ds(x, y, i, j)


def solve(x, y, d1, d2):
    global board, n, ans, total_sum

    checked = [[5 for _ in range(n)] for _ in range(n)]
    min_p = 40001
    max_p = 0

    # 1
    fir = 0
    for i in range(x):
        for j in range(y+1):
            checked[i][j] = 1
            fir += board[i][j]
    for i in range(x, x+d1):
        for j in range(y-i+x):
            checked[i][j] = 1
            fir += board[i][j]
    min_p = min(min_p, fir)
    max_p = max(max_p, fir)

    # 2
    sec = 0
    for i in range(x):
        for j in range(y+1, n):
            checked[i][j] = 2
            sec += board[i][j]
    for i in range(x, x+d2+1):
        for j in range(y+1+i-x, n):
            checked[i][j] = 2
            sec += board[i][j]
    min_p = min(min_p, sec)
    max_p = max(max_p, sec)

    # 3
    thir = 0
    for i in range(x+d1, x+d1+d2+1):
        for j in range(y - d1 + i - (x+d1)):
            checked[i][j] = 3
            thir += board[i][j]
    for i in range(x+d1+d2+1, n):
        for j in range(y-d1+d2):
            checked[i][j] = 3
            thir += board[i][j]
    min_p = min(min_p, thir)
    max_p = max(max_p, thir)

    # 4
    forth = 0
    for i in range(x+d2+1, x+d1+d2+1):
        for j in range(y+d2-i+(x+d2+1), n):
            checked[i][j] = 4
            forth += board[i][j]

    for i in range(x+d1+d2+1, n):
        for j in range(y-d1+d2, n):
            checked[i][j] = 4
            forth += board[i][j]
    min_p = min(min_p, forth)
    max_p = max(max_p, forth)

    # 5
    fifth = total_sum - (fir + sec + thir + forth)
    min_p = min(min_p, fifth)
    max_p = max(max_p, fifth)

    ans = min(ans, abs(max_p - min_p))


n = int(sys.stdin.readline().strip())
board = []
for _ in range(n):
    board.append(list(map(int, sys.stdin.readline().strip().split(" "))))

# 5번 구역의 인구수를 구하기 위함
total_sum = 0
for i in range(n):
    total_sum += sum(board[i])

# 답 구하기
ans = 40001
for i in range(0, n-1):
    for j in range(1, n-1):
        choice_ds(i, j, 0, 0)
print(ans)