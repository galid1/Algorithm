import sys, heapq


def solve():
    global x, y, board, t

    ans = 0
    for i in range(x - 2):
        for j in range(y - 2):
            copied = copy_nine(i, j)

            for _ in range(4):
                heapq.heappop(copied)

            if heapq.heappop(copied) >= t:
                ans += 1

    print(ans)


def copy_nine(si, sj):
    global board

    copied = []

    for i in range(si, si + 3):
        for j in range(sj, sj + 3):
            heapq.heappush(copied, board[i][j])

    return copied


x, y = map(int, sys.stdin.readline().strip().split(" "))
board = []
for _ in range(x):
    board.append(list(map(int, sys.stdin.readline().strip().split(" "))))

t = int(sys.stdin.readline().strip())
solve()
