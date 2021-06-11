import sys


def solve():
    global l, s, n

    s.sort()

    a, b = 0, 0

    for idx, num in enumerate(s):
        # 같은 수가 있으면 무조건 0
        if num == n:
            return print(0)

        if a < num < n:
            a = num

        if num > n:
            b = num
            break

    ans = (n-(a+1)+1) * ((b-1)-n+1) - 1
    print(ans)


l = int(sys.stdin.readline().strip())
s = list(map(int, sys.stdin.readline().strip().split(" ")))
n = int(sys.stdin.readline().strip())

solve()