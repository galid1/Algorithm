import sys


def solution():
    global nums

    idx = -1
    max_num = -1
    for i in range(len(nums)):
        if max_num < nums[i]:
            idx = i
            max_num = nums[i]

    print(max_num)
    print(idx + 1)


nums = []
for i in range(9):
    nums.append(int(sys.stdin.readline()))

solution()