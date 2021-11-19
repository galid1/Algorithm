import sys


def solve():
    global l, r

    if len(l) != len(r):
        return print(0)

    ans = 0
    for i in range(len(l)):
        if int(l[i]) < int(r[i]):
            return print(ans)

        if l[i] != '8':
            continue

        if int(r[i]) >= 9:
            return print(ans)

        ans += 1

    print(ans)



l, r = sys.stdin.readline().strip().split(" ")
solve()