import sys
sys.setrecursionlimit(1000000)


def solve(ci):
    global n, board, ds

    for i in range(1, board[ci] + 1):
        ni = ci + i

        if ni >= n:
            continue

        if ds[ni] > ds[ci] + 1:
            ds[ni] = ds[ci] + 1
            solve(ni)


n = int(sys.stdin.readline().strip())
ds = [sys.maxsize for _ in range(n)]
ds[0] = 0
board = list(map(int, sys.stdin.readline().strip().split(" ")))
solve(0)

if ds[-1] == sys.maxsize:
    print(-1)
else:
    print(ds[-1])

# 10
# 5 1 3 1 2 1 4 1 1 1

# 25
# 0 11 3 1 8 11 2 2 1 6 5 10 1 4 5 3 6 9 5 10 3 10 3 0 7

# 8
# 2 2 2 2 2 2 3 1

# 15
# 4 5 2 5 5 4 0 1 3 4 1 2 0 2 3

# 6
# 0 0 1 0 1 1

# 8
# 5 1 1 1 4 1 2 1