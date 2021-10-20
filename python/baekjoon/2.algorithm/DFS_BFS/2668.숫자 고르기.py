import sys


def solve():
    global n, g

    ans = set()
    for i in range(1, n+1):
        if i in ans:
            continue

        if dfs(i, i, ans):
            ans.add(i)

    ans = sorted(ans)
    print(len(ans))
    for num in ans:
        print(num)


def dfs(s, v, ans):
    global g

    nv = g[v]

    if nv == s:
        return True

    if nv in ans:
        return False

    ans.add(nv)
    res = dfs(s, nv, ans)

    if not res:
        ans.remove(nv)
    return res


n = int(sys.stdin.readline().strip())
g = {}
for i in range(1, n+1):
    to = int(sys.stdin.readline().strip())
    g[i] = to

solve()

# 7
# 3
# 1
# 1
# 5
# 5
# 4
# 6

# 6
# 2
# 3
# 1
# 5
# 6
# 4

# 10
# 2
# 4
# 1
# 7
# 7
# 4
# 4
# 8
# 2
# 1

# 9
# 5
# 6
# 2
# 8
# 3
# 4
# 2
# 7
# 6