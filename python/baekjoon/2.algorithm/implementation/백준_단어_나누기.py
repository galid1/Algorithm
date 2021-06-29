import sys


def solve():
    global s

    for i in range(len(s)-2):
        for j in range(i+1, len(s)-1):
            remix(i, j)


def remix(first, second):
    global s, ans

    remixed = s[first::-1] + s[second:first:-1] + s[-1:second:-1]

    if ans == '':
        ans = remixed
        return

    if ans > remixed:
        ans = remixed


s = sys.stdin.readline().strip()
ans = ''
solve()
print(ans)
