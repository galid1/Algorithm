import sys


def solve(i, cur_sum):
    global n, s, nums, ans

    if cur_sum == s:
        ans += 1

    for j in range(i+1, n):
        solve(j, cur_sum + nums[j])


n, s = map(int, sys.stdin.readline().strip().split(' '))
nums = list(map(int, sys.stdin.readline().strip().split(" ")))

ans = 0
for i in range(n):
    solve(i, nums[i])

print(ans)