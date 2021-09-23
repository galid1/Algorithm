import sys


def solve(ops, cur_num, cur_str):
    global n, nums

    if len(ops) == n-1:
        if cal(nums, ops) == 0:
            print(cur_str)
        return

    for op in [' ', '+', '-']:
        ops.append(op)
        solve(ops, cur_num+1, cur_str + op + str(cur_num))
        ops.pop()




def cal(nums, ops):
    def do_cal(added, adder, op):
        if op == '+':
            return int(added) + int(adder)
        elif op == '-':
            return int(added) - int(adder)

    res, n_idx = make_num(0, nums, ops)
    op = ''

    while n_idx < len(nums):
        op = ops[n_idx - 1]
        adder, n_idx = make_num(n_idx, nums, ops)
        res = do_cal(res, adder, op)

    return res


def make_num(n_idx, nums, ops):
    res = str(nums[n_idx])
    n_idx += 1

    while n_idx < len(nums):
        if ops[n_idx - 1] != ' ':
            break

        res += str(nums[n_idx])
        n_idx += 1

    return res, n_idx



t = int(sys.stdin.readline().strip())
for _ in range(t):
    n = int(sys.stdin.readline().strip())
    nums = [i for i in range(1, n+1)]
    solve([], 2, '1')
    print("")