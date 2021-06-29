import sys

def solution(m, nums):
    answers = []

    visit = [0 for i in range(len(nums))]

    for i in range(len(nums)):
        if i <= m:
            visit[i] = 1
            recur(nums, m, answers, visit, sums=[nums[i]])
            visit[i] = 0

    res = max(answers)
    print(res)


def recur(nums, m, answers, visit, sums):
    if len(sums) == 3:
        res = sum(sums)
        if res <= m:
            answers.append(res)
        return

    for i in range(len(nums)):
        if not visit[i]:
            if sum(sums) + nums[i] <= m:
                visit[i] = 1
                sums.append(nums[i])
                recur(nums, m, answers, visit, sums)
                visit[i] = 0
                sums.pop()




n, m = map(int, sys.stdin.readline().split(" "))
nums = list(map(int, sys.stdin.readline().split(" ")))
solution(m, nums)
