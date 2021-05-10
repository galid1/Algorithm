import sys


def solve():
    global r, s

    n_s = ''

    for i in range(len(s)):
        for j in range(r):
            n_s += s[i]

    print(n_s)


t = int(sys.stdin.readline().strip())
for _ in range(t):
    r, s = sys.stdin.readline().strip().split(" ")
    r = int(r)
    solve()