import sys
from collections import Counter, defaultdict


def solve():
    global board

    cnts = Counter(board)

    ans = 0
    for row, cnt in cnts.items():
        if valid(row):
            ans = max(ans, cnt)

    print(ans)


def valid(row):
    global k, n, m

    on_off_cnt = Counter(list(row))

    if on_off_cnt['0'] > k:
        return False

    if on_off_cnt['0']%2 != k%2:
        return False

    return True


n, m = map(int, sys.stdin.readline().strip().split(" "))
board = []
for _ in range(n):
    board.append(sys.stdin.readline().strip())

k = int(sys.stdin.readline().strip())
ans = 0
solve()


# 4 4
# 0100
# 1000
# 0000
# 0000
# 2

# 8 3
# 000
# 001
# 010
# 011
# 100
# 101
# 110
# 111

