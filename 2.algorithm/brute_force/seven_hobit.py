import sys

def search(nums):
    for i in range(0, 8):
        for j in range(i+1, 9):
            sum = 0

            for k in range(0,9):
                if k is not i and k is not j:
                    sum += nums[k]

            if sum is 100:
                for m in range(0, 9):
                    if m is i or m is j:
                        continue
                    print(nums[m])
            return

nums = list(map(int, sys.stdin.readline().split(" ")))
search(nums)