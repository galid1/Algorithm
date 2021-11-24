import sys


def solve():
    global n, ws

    ans = 0
    while ws:
        w = ws.pop(0)
        ans += 1

        for _ in range(len(w)):
            if w in ws:
                ws.remove(w)
            w = shuffle(w)

    print(ans)


def shuffle(w):
    return w[1:] + w[0]


n = int(sys.stdin.readline().strip())
ws = []
for _ in range(n):
    ws.append(sys.stdin.readline().strip())

solve()

# 6
# aaaa
# aaaa
# aaa
# aa
# aaaa
# aaaaa