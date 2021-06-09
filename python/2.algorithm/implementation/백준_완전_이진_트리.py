import sys

def solve(depth, start_i, end_i, cur_len):
    global k, nodes, trees

    half_idx = (start_i + end_i) // 2
    trees[depth].append(nodes[half_idx])

    if cur_len == 1:
        return

    next_len = cur_len // 2
    solve(depth + 1, start_i, half_idx - 1, next_len)
    solve(depth + 1, half_idx + 1, end_i, next_len)



k = int(sys.stdin.readline().strip())
nodes = list(map(int, sys.stdin.readline().strip().split(" ")))
trees = [[] for _ in range(k)]
solve(0, 0, len(nodes)-1, len(nodes))
for layer in trees:
    print(*layer)