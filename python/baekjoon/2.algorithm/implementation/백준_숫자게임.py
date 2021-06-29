import sys


def solve(cur_i, nums):
    global ans, max_num

    res = 0
    max_last_digit = 0
    for i in range(3):
        res += nums[i]
        for j in range(i+1, 4):
            res += nums[j]
            for k in range(j+1, 5):
                res += nums[k]

                last_digit_num = int(str(res)[-1])
                if last_digit_num > max_last_digit:
                    max_last_digit = last_digit_num
                res -= nums[k]
            res -= nums[j]
        res -= nums[i]

    if max_last_digit >= max_num:
        max_num = max_last_digit
        ans = cur_i


n = int(sys.stdin.readline().strip())
max_num = 0
ans = 1
for i in range(n):
    solve(i+1, list(map(int, sys.stdin.readline().strip().split(" "))))

print(ans)