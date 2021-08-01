import sys


def solve(n, grade, p, nums):
    # 현재 점수와 grade 같을 때 까지 rank, idx를 계속 올린다.
    # idx가 p와 같다면 -1을 리턴
    # 현재 점수와 grade가 같다면, 같지 않을때까지 idx를 증가 p와 같다면 -1 리턴
    idx, rank = 0, 1
    while idx < n:
        if nums[idx] < grade:
            return print(rank)

        flag = False
        while idx < n and grade == nums[idx]:
            flag = True
            idx, rank = idx+1, rank+1
            if idx + 1 > p:
                return print(-1)

        if flag:
            return print(rank-1)

        idx, rank = idx + 1, rank + 1

    if idx+1 > p:
        return print(-1)
    print(rank-1)


n, grade, p = map(int, sys.stdin.readline().strip().split(" "))
nums_s = sys.stdin.readline().strip()
if not nums_s:
    print(1)
    exit()
nums = list(map(int, nums_s.split(" ")))
solve(n, grade, p, nums)

# 3 5 3
# 30 20 10

# 4 80 4
# 100 90 90 80

# 0 10 1

# 6 3 5
# 10 10 10 10 5 4

# 4 20 4
# 10 10 10 10

# 4 10 4
# 10 10 10 10

# 3 10 3
# 20 10 10
# -1!


# 5 2 5
# 6 5 4 3 1
# 5!