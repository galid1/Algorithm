import sys


def solve(paths):
    linked_map = init_map()

    root = linked_map[paths[0]]
    for path in paths[1:]:
        if linked_map[path] != root:
            return print("NO")
    print("YES")


def init_map():
    global n, board

    linked_map = [i for i in range(n)]

    for i in range(n):
        for j in range(n):
            if i == j:
                continue

            if linked_map[i] == linked_map[j]:
                continue

            if board[i][j]:
                union(linked_map, i, j)

    return linked_map



def union(linked_map, f, t):
    root_f = find(f, linked_map)
    root_t = find(t, linked_map)

    root = root_f if root_f < root_t else root_t

    linked_map[root_f] = root
    linked_map[root_t] = root


def find(node, linked_map):
    if node == linked_map[node]:
        return node

    root = find(linked_map[node], linked_map)
    linked_map[node] = root
    return root


n = int(sys.stdin.readline().strip())
m = int(sys.stdin.readline().strip())
board = []
for _ in range(n):
    board.append(list(map(int, sys.stdin.readline().strip().split(" "))))

paths = list(map(lambda item: int(item) - 1, sys.stdin.readline().strip().split(" ")))
solve(paths)


# 1-2-4
#     I
#   3-5
#
# 5
# 2
# 0 1 0 0 0
# 1 0 0 1 0
# 0 0 0 0 1
# 0 1 0 0 1
# 0 0 1 1 0
# 1 5