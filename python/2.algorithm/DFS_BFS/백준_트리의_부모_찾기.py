import sys
from collections import deque


def solution():
    global n, tree

    answer = {i:0 for i in range(2, n+1)}
    v = [0 for _ in range(n+1)]
    q = deque()
    q.append(1)
    v[1] = 1

    while q:
        parent = q.pop()
        for c in tree[parent]:
            if v[c]:
                continue

            answer[c] = parent
            v[c] = 1
            q.append(c)

    for p in answer.values():
        print(p)


n = int(sys.stdin.readline())
tree = {i:[] for i in range(1, n+1)}
for i in range(n-1):
    k, v = map(int, sys.stdin.readline().strip().split(" "))
    tree[k].append(v)
    tree[v].append(k)

solution()