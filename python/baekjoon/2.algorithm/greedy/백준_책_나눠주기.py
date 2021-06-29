import sys

def solve():
    global n, m, abs
    # b, a 순으로 들어가 있음(b기준으로 정렬을 위해서)
    abs.sort()

    res = 0
    visited = [False for _ in range(n+1)]
    for b, a in abs:
        for i in range(a, b+1):
            if not visited[i]:
                visited[i] = True
                res += 1
                break

    print(min(res, n))


t = int(sys.stdin.readline().strip())
for _ in range(t):
    n, m = list(map(int, sys.stdin.readline().strip().split(" ")))
    abs = []
    for _ in range(m):
        a, b, = map(int, sys.stdin.readline().strip().split(" "))
        abs.append((b, a))
    solve()

# 1
# 4 7
# 1 5
# 2 3
# 3 6
# 4 5
# 6 7
# 1 3
# 2 2

# 1
# 5 4
# 2 2
# 3 3
# 1 5
# 1 5
# 1 5

