import sys

def solve():
    global n, m, root_idx

    # 트리 만들기
    tree = make_tree()
    del_node(tree)

    if m == root_idx:
        return print(0)

    ans = 0
    stack = [root_idx]
    while stack:
        c = stack.pop()

        if not tree[c]:
            ans += 1
            continue

        stack += tree[c]

    print(ans)



def make_tree():
    global n, m, ps, root_idx

    tree = {i:[] for i in range(n+1)}

    idx = -1
    for i in range(n):
        idx += 1

        if ps[i] == -1:
            root_idx = idx
            continue

        if idx == m:
            continue

        tree[ps[i]].append(idx)

    return tree


def del_node(tree):
    global m

    stack = [m]

    while stack:
        c = stack.pop()

        for link in tree[c]:
            stack.append(link)

        tree[c] = []



n = int(sys.stdin.readline().strip())
ps = list(map(int, sys.stdin.readline().strip().split(" ")))
m = int(sys.stdin.readline().strip())
root_idx = -1
solve()

# 5
# -1 0 0 1 1
# 2

# 7
# 3 6 6 -1 0 6 3
# 4