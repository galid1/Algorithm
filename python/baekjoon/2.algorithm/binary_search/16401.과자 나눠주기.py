import sys


def solve():
    global m, n, ss

    if sum(ss) < m:
        return print(0)

    ss.sort(reverse=True)

    l, r = 1, ss[0]
    ans = -1
    while l <= r:
        target_length = (l+r) // 2

        if sharable(target_length, ss):
            ans = target_length
            l = target_length + 1
        else:
            r = target_length - 1

    print(ans)


def sharable(target_length, ss):
    cnt = 0

    for snack_length in ss:
        if snack_length < target_length:
            break
        cnt += snack_length // target_length

    return cnt >= m

m, n = map(int, sys.stdin.readline().strip().split(" "))
ss = list(map(int, sys.stdin.readline().strip().split(" ")))

solve()
