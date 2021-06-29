import sys


def solve():
    global n

    if sum(map(int, n)) % 3 != 0:
        return print(-1)

    n.sort(reverse=True)

    if n[-1] != '0':
        return print(-1)

    print(''.join(n))




n = list(sys.stdin.readline().strip())
solve()
