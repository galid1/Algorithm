import sys

def recur(length, cur, visit, next_idx):
    global ans, l, r, x, a

    if len(cur) == length:
        if l <= sum(cur) <= r:
            if cur[-1] - cur[0] >= x:
                ans += 1
        return

    for i in range(next_idx, len(a)):
        cur.append(a[i])
        visit[i] = True
        recur(length, cur, visit, i+1)
        cur.pop()
        visit[i] = False


def solution():
    global n

    a.sort()
    for length in range(2, len(a)+1):
        recur(length, [], [False for _ in range(len(a)+1)], 0)

    print(ans)

ans = 0
n, l, r, x = map(int, sys.stdin.readline().strip().split(" "))
a = list(map(int, sys.stdin.readline().strip().split(" ")))

solution()

# 3 5 6 1
# 1 2 3