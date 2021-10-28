import sys
sys.setrecursionlimit(10**9)

def solve(in_l, in_r, post_l, post_r):
    global n, in_order, post_order, in_order_position

    if in_l > in_r:
        return

    root = post_order[post_r]
    print(root, end=' ')

    if in_l == in_r:
        return

    root_position_in_order = in_order_position[root]
    left_cnt = root_position_in_order - in_l

    solve(in_l, root_position_in_order-1, post_l, post_l + left_cnt - 1)
    solve(root_position_in_order + 1, in_r, post_l + left_cnt, post_r - 1)




def make_in_order_position(in_order):
    in_order_position = [-1 for _ in range(n + 1)]
    for i in range(len(in_order)):
        in_order_position[in_order[i]] = i

    return in_order_position


n = int(sys.stdin.readline().strip())
in_order = list(map(int, sys.stdin.readline().strip().split(" ")))
post_order = list(map(int, sys.stdin.readline().strip().split(" ")))
in_order_position = make_in_order_position(in_order)

solve(0, n-1, 0, n-1)
