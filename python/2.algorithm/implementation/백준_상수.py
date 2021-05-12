import sys


def solve():
    global a, b

    a = int(a[-1::-1])
    b = int(b[-1::-1])

    print(a) if a > b else print(b)


a, b = sys.stdin.readline().strip().split(" ")
solve()