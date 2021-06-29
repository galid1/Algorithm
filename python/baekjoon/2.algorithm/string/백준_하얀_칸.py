import sys


def solve():
    global board

    start = 0
    ans = 0
    for i in range(8):
        for j in range(start, 8, 2):
            if board[i][j] == 'F':
                ans += 1
        start = (start + 1) % 2

    print(ans)


board = []
for _ in range(8):
    board.append(list(sys.stdin.readline().strip()))
solve()