import sys


def solve():
    global n, m, cmds, ps

    for cmd, n1, n2 in cmds:
        if cmd == 0:
            union(n1, n2)
        else:
            if find(n1) == find(n2):
                print("YES")
            else:
                print("NO")


def find(node):
    global ps

    if node == ps[node]:
        return ps[node]

    root = find(ps[node])
    ps[node] = root
    return root


def union(n1, n2):
    global ps

    p1 = find(n1)
    p2 = find(n2)

    root = p1 if p1 < p2 else p2
    ps[p1] = root
    ps[p2] = root


n, m = map(int, sys.stdin.readline().strip().split(" "))
ps = [i for i in range(n+1)]
cmds = []
for _ in range(m):
    cmds.append(list(map(int, sys.stdin.readline().strip().split(" "))))

solve()

# 5 4
# 0 1 2
# 0 2 4
# 0 3 5
# 0 4 5

