import sys


def solve(n, grade, p, nums):
    idx, rank = 0, 1

    while True:
        if grade > nums[idx]:
            return print(rank)
        elif grade == nums[idx]:
            while grade == nums[idx]:
                idx = idx + 1
                if idx >= p:
                    return print(-1)
                if idx >= n:
                    return print(rank)
        else:
            idx, rank = idx+1, rank+1
            if idx >= p:
                return print(-1)
            if idx >= n:
                return print(rank)


n, grade, p = map(int, sys.stdin.readline().strip().split(" "))
nums_s = sys.stdin.readline().strip()
if not nums_s:
    print(1)
    exit()
nums = list(map(int, nums_s.split(" ")))
solve(n, grade, p, nums)

# 3 5 3
# 30 20 10

# 4 80 5
# 100 90 90 80

# 0 10 1

# 6 3 5
# 10 10 10 10 5 4

# 4 20 4
# 10 10 10 10

# 4 10 5
# 10 10 10 10

# 3 10 3
# 20 10 10
# -1!


# 5 2 5
# 6 5 4 3 1
# 5!