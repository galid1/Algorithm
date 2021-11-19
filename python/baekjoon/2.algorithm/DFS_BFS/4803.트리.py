import sys


def solve(case):
    global n, m, g, visited

    ans = 0
    for i in range(n):
        if visited[i]:
            continue

        is_tree = dfs(i)

        if is_tree:
            ans += 1

    if ans == 0:
        print('Case {}: No trees.'.format(case))
    elif ans == 1:
        print('Case {}: There is one tree.'.format(case))
    else:
        print('Case {}: A forest of {} trees.'.format(case, ans))
    # if ans == 0:
    #     print("Case %d: No trees." %(case))
    # elif ans == 1:
    #     print("Case %d: There is one tree." %(case))
    # else:
    #     print("Case %d: A forest of %d trees." %(case, ans))

def dfs(i):
    global g, visited

    is_tree = True
    stack = [[i, -1]]
    visited[i] = True
    cur, bef = -1, -1
    while stack:
        cur, bef = stack.pop()

        for to in g[cur]:
            if to == bef:
                continue

            if visited[to]:
                is_tree = False
                continue

            visited[to] = True
            stack.append([to, cur])

    return is_tree


case = 0
while True:
    n, m = map(int, sys.stdin.readline().strip().split(" "))
    if n == 0 and m == 0:
        break
    case += 1
    g = [[] for _ in range(n)]
    for _ in range(m):
        f, t = map(lambda item: int(item) - 1, sys.stdin.readline().strip().split(" "))
        g[f].append(t)

        if f == t:
            continue
        g[t].append(f)

    visited = [False for _ in range(n)]
    solve(case)



# 6 3
# 1 2
# 2 3
# 3 4
# 0 0

# 6 6
# 1 2
# 2 3
# 2 6
# 3 6
# 4 4
# 4 5
