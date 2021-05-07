import sys


def solve():
    global r, b

    point = (r - 4) // 2

    for x in range(1, point):
        y = point - x

        if x * y == b:
            ans = [x + 2, y + 2]
            ans.sort(reverse=True)
            return print(*ans)


r, b = map(int, sys.stdin.readline().strip().split(" "))
solve()
