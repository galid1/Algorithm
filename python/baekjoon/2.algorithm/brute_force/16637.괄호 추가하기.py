import sys


def solve(idx, acc):
    global nums, ops, n, ans

    if idx == len(ops):
        ans = max(ans, acc)
        return

    solve(idx+1, cal(acc, nums[idx+1], ops[idx]))

    if idx + 1 < len(ops):
        b_r = cal(nums[idx+1], nums[idx+2], ops[idx+1])
        solve(idx+2, cal(acc, b_r, ops[idx]))


def cal(operand1, operand2, operator):
    if operator == '+':
        return operand1 + operand2
    elif operator == '*':
        return operand1 * operand2
    elif operator == '-':
        return operand1 - operand2


n = int(sys.stdin.readline().strip())
nums, ops = [], []
for c in list(sys.stdin.readline().strip()):
    if c.isnumeric():
        nums.append(int(c))
    else:
        ops.append(c)

ans = -sys.maxsize
solve(0, nums[0])
print(ans)