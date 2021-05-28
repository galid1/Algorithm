import sys


def solve():
    global ss
    print(ss)


ss = []
while True:
    s = sys.stdin.readline().strip()
    if s == '*':
        break

    ss.append(list(s))

solve()