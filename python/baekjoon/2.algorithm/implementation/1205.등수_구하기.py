import sys


def solve(n, grade, p, nums):
    idx, rank = -1, 0

    while idx + 1 < n:
        idx, rank = idx+1, rank+1

        if grade >= nums[idx]:
            while idx < n and grade == nums[idx]:
                idx += 1
                if idx >= p:
                    return print(-1)

            return print(rank)
    if idx >= p:
        return print(-1)
    print(rank)


n, grade, p = map(int, sys.stdin.readline().strip().split(" "))
nums_s = sys.stdin.readline().strip()
if not nums_s:
    print(1)
    exit()
nums = list(map(int, nums_s.split(" ")))
solve(n, grade, p, nums)


# 4 80 4
# 100 90 90 80

# 0 10 1

# 6 3 5
# 10 10 10 10 5 4

# 4 20 5
# 10 10 10 10