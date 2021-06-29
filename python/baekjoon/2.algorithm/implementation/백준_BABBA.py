import sys


def solve():
    global n

    a, b = 1, 0

    for _ in range(n):
        will_a = b
        will_b = a+b

        a, b = will_a, will_b

    print(a, b)


n = int(sys.stdin.readline().strip())
solve()