import sys


def solve():
    global n, ss

    res = ''
    for i in range(len(ss[0])):
        all_same = True
        c = ss[0][i]
        for j in range(1, len(ss)):
            if ss[j][i] != c:
                all_same = False
                break

        if all_same:
            res += c
        else:
            res += '?'

    print(res)

n = int(sys.stdin.readline().strip())
ss = []
for _ in range(n):
    ss.append(sys.stdin.readline().strip())
solve()

