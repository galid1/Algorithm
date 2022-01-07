import sys


def solve():
    global s, t

    if len(s) > len(t):
        s, t = t, s

    dy = [[0 for _ in range(max(len(s), len(t)) + 1)]
          for _ in range(min(len(s), len(t)) + 1)]

    ans = 0
    for i in range(1, len(s)):
        for j in range(1, len(t)):
            if s[i] == t[j]:
                dy[i][j] = dy[i - 1][j - 1] + 1
                ans = max(dy[i][j], ans)
    print(ans)


s = sys.stdin.readline().strip()
t = sys.stdin.readline().strip()

solve()

