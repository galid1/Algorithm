import sys


def solve(selected_ops):
    global n, nums, ops

    if len(selected_ops) >= len(nums) - 1:
        cal_exp(selected_ops)
        return

    for i in range(4):
        if is_valid(i):
            ops[i] -= 1
            selected_ops.append(i)
            solve(selected_ops)
            selected_ops.pop()
            ops[i] += 1


def cal_exp(ops):
    global nums, min_num, max_num

    res = nums[0]
    for i in range(0, len(nums)-1):
        if ops[i] == 0:
            res += nums[i+1]
        elif ops[i] == 1:
            res -= nums[i+1]
        elif ops[i] == 2:
            res *= nums[i+1]
        elif ops[i] == 3:
            if (res < 0 and nums[i+1] > 0) or (res > 0 and nums[i+1] < 0):
                res = abs(res) // abs(nums[i+1])
                res = -res
            else:
                res //= nums[i + 1]

    min_num = min(min_num, res)
    max_num = max(max_num, res)


def is_valid(ops_idx):
    global ops

    if ops[ops_idx] >= 1:
        return True
    return False



n = int(sys.stdin.readline().strip())
nums = list(map(int, sys.stdin.readline().strip().split(" ")))
ops = list(map(int, sys.stdin.readline().strip().split(" ")))
min_num = sys.maxsize
max_num = -sys.maxsize - 1
solve([])
print(max_num)
print(min_num)
