import sys


def solve():
    global n, nums

    nums.sort(reverse=True)

    ans = 0
    idx = 0
    zero = False
    neg = False
    while idx < n - 1:
        if nums[idx] > 1:
            if nums[idx + 1] > 1:
                ans += (nums[idx] * nums[idx + 1])
                idx += 2
            elif nums[idx + 1] == 1:
                ans += nums[idx] + nums[idx + 1]
                idx += 2
            else:
                ans += nums[idx]
                idx += 1

        elif nums[idx] == 1:
            ans += nums[idx]
            idx += 1

        elif nums[idx] == 0:
            zero = True
            idx += 1

        else:
            neg = True
            break

    if neg:
        neg_nums = nums[idx:]
        neg_nums.sort()
        idx = 0
        while idx < len(neg_nums) - 1:
            ans += (neg_nums[idx] * neg_nums[idx + 1])
            idx += 2

        if idx == len(neg_nums) - 1 and not zero:
            ans += neg_nums[idx]

    else:
        if idx == n-1:
            if nums[idx] >= 0 or not zero:
                ans += nums[idx]

    print(ans)


# 7
# 3
# 2
# 0
# 0
# -1
# -2
# -3

n = int(sys.stdin.readline().strip())
nums = []
for _ in range(n):
    nums.append(int(sys.stdin.readline().strip()))

solve()
