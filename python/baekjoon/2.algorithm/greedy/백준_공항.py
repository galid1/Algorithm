import sys, heapq
from collections import deque

def find_parent(pi):
    global parents

    if parents[pi] == pi:
        return pi
    p = find_parent(parents[pi])
    parents[pi] = p
    return p


def union(x, y):
    global parents
    px = find_parent(x)
    py = find_parent(y)
    parents[px] = py


def solve():
    global g, p, ps, parents
    ans = 0

    for pi in ps:
        parent = find_parent(pi)

        if parent == 0:
            break
        ans += 1
        union(parent, parent-1)

    print(ans)


g = int(sys.stdin.readline().strip())
p = int(sys.stdin.readline().strip())
ps = deque()
parents = {i:i for i in range(0, g+1)}
for i in range(p):
    ps.append(int(sys.stdin.readline().strip()))
solve()

