import sys

def solve(ans, cur, idx, plus, minus, mul, div):
    global n, nums

    if idx == n:
        ans[0] = min(ans[0], cur)
        ans[1] = max(ans[1], cur)
        return

    if plus >= 1:
        solve(ans, cur+nums[idx], idx+1, plus-1, minus, mul, div)
    if minus >= 1:
        solve(ans, cur-nums[idx], idx+1, plus, minus-1, mul, div)
    if mul >= 1:
        solve(ans, cur*nums[idx], idx+1, plus, minus, mul-1, div)
    if div >= 1:
        if cur >= 0:
            solve(ans, cur//nums[idx], idx+1, plus, minus, mul, div-1)
        else:
            solve(ans, -(-cur//nums[idx]), idx+1, plus, minus, mul, div-1)


n = int(sys.stdin.readline().strip())
nums = list(map(int, sys.stdin.readline().strip().split(" ")))
ops = list(map(int, sys.stdin.readline().strip().split(" ")))

ans = [sys.maxsize, -sys.maxsize]
solve(ans, nums[0], 1, *ops)
print(ans[1])
print(ans[0])
