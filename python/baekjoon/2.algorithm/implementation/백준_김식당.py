import sys


def solve(cmd):
    global orders

    op = cmd[0]

    if op == "order":
        n, t = int(cmd[1]), int(cmd[2])
        orders.append([n, t])
    elif op == "sort":
        orders.sort(key=lambda item: item[0])
        orders.sort(key=lambda item: item[1])
    elif op == "complete":
        n = int(cmd[1])
        will_delete_idx = -1

        for idx, order_info in enumerate(orders):
            if n == order_info[0]:
                will_delete_idx = idx
                break

        if will_delete_idx != -1:
            del orders[will_delete_idx]

    if not orders:
        print("sleep")
    else:
        order_list = ''
        for order in orders:
            order_list += str(order[0]) + ' '
        print(order_list)


n, m = map(int, sys.stdin.readline().strip().split(" "))
orders = []
for _ in range(n):
    solve(sys.stdin.readline().strip().split(" "))


# 9 5
# order 2 2
# order 1 2
# sort
# complete 1
# sort
# complete 2
# sort
# order 3 1
# order 4 2


# 7 3
# order 1 4
# order 2 2
# order 3 3
# sort
# complete 3
# complete 2
# complete 1


# 15 6
# order 2 1
# order 1 1
# order 10 1
# sort
# complete 2
# complete 1