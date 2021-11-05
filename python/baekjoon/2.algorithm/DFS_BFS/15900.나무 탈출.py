import sys
from collections import deque


def solve():
    global n, tree

    visited = [False for _ in range(n + 1)]

    stack = [[1, 0]]
    leaf_sums = 0

    while stack:
        cur, depth = stack.pop()
        visited[cur] = True

        leaf = True
        for link in tree[cur]:
            if visited[link]:
                continue
            stack.append([link, depth + 1])
            leaf = False

        if leaf:
            leaf_sums += depth

    if leaf_sums%2 != 0:
        print("Yes")
    else:
        print("No")


n = int(sys.stdin.readline().strip())
edges = []
for i in range(n - 1):
    f, t = map(int, sys.stdin.readline().strip().split(" "))
    edges.append([f, t])

tree = {i: set() for i in range(1, n + 1)}
while edges:
    f, t = edges.pop()
    tree[f].add(t)
    tree[t].add(f)

solve()
