import sys


def dfs(res):
    global nums

    if len(res) == 7:
        print("=-=====")
        print(sum(res))
        return




nums = []

for i in range(9):
    nums.append(int(sys.stdin.readline()))

print(nums)