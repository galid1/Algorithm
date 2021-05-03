import sys


def solve():
    global ss

    res = ''
    for s in ss:
        res += s[0]

    print(res)


ss = sys.stdin.readline().strip().split("-")
solve()