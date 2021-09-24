import sys


def solve(cur, weight):
    global n, nums, max_num

    if cur == n:
        if 0 < weight <= max_num:
            board[weight] = True
        return

    solve(cur + 1, weight + nums[cur])
    solve(cur + 1, weight - nums[cur])
    solve(cur + 1, weight)



n = int(sys.stdin.readline().strip())
nums = list(map(int, sys.stdin.readline().strip().split(" ")))
max_num = sum(nums)
board = [False for _ in range(max_num + 1)]
solve(0, 0)

res = 0
for possible in board[1:]:
    if not possible:
        res += 1
print(res)