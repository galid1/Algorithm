import sys


def solve():
    global nums

    ans = 0
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            if nums[i]*2 == nums[j]:
                ans += 1
                break
    print(ans)


while True:
    inputs = sys.stdin.readline().strip()
    if inputs == '-1':
        break

    nums = list(map(int, inputs.split(" ")))
    nums.sort()
    solve()