import sys


def solve():
    global n, m, board

    # 1. 가로 최대, 세로 유동적
    fir()

    # 2. 세로 최대, 가로 유동적
    sec()

    # 3. 첫 사각형 두번째 사각형 가로 나누기
    third()

    # 4. 세로 나누기
    forth()

    # 5. 두번째, 세번째 사각형 가로 나누기
    fifth()

    # 6. 두번째, 세번째 사각형 세로 나누기
    sixth()


def my_sum(xs, xe, ys, ye):
    global board

    result = 0
    for i in range(xs, xe):
        for j in range(ys, ye):
            result += board[i][j]

    return result

def update_ans(fir_sum, sec_sum):
    global ans, total_sum
    thi_sum = total_sum - (fir_sum + sec_sum)
    ans = max(ans, fir_sum * sec_sum * thi_sum)


def fir():
    global board, n, m, ans, total_sum

    for fir_row in range(n-2):
        for sec_row in range(fir_row + 1, n-1):
            fir_sum = my_sum(0, fir_row+1, 0, m)
            sec_sum = my_sum(fir_row+1, sec_row+1, 0, m)
            update_ans(fir_sum, sec_sum)


def sec():
    global board, n, m, ans, total_sum

    for fir_col in range(m-2):
        for sec_col in range(fir_col + 1, m-1):
            fir_sum = my_sum(0, n, 0, fir_col + 1)
            sec_sum = my_sum(0, n, fir_col + 1, sec_col + 1)
            update_ans(fir_sum, sec_sum)


def third():
    global board, n, m, ans, total_sum

    for row in range(n-1):
        for col in range(m-1):
            fir_sum = my_sum(0, row+1, 0, col+1)
            sec_sum = my_sum(0, row+1, col+1, m)
            update_ans(fir_sum, sec_sum)


def forth():
    global board, n, m, ans, total_sum

    for col in range(m-1):
        for row in range(n-1):
            fir_sum = my_sum(0, row+1, 0, col+1)
            sec_sum = my_sum(row+1, n, 0, col+1)
            update_ans(fir_sum, sec_sum)


def fifth():
    global board, n, m, ans, total_sum

    for row in range(n-1):
        fir_sum = my_sum(0, row+1, 0, m)

        for col in range(m-1):
            sec_sum = my_sum(row+1, n, 0, col+1)
            update_ans(fir_sum, sec_sum)


def sixth():
    global board, n, m, ans, total_sum

    for col in range(m-1):
        fir_sum = my_sum(0, n, 0, col+1)

        for row in range(n-1):
            sec_sum = my_sum(0, row+1, col+1, m)
            update_ans(fir_sum, sec_sum)


n, m = map(int, sys.stdin.readline().strip().split(" "))
board = []
total_sum = 0
for _ in range(n):
    line = list(map(int, list(sys.stdin.readline().strip())))
    total_sum += sum(line)
    board.append(line)

ans = 0
solve()
print(ans)