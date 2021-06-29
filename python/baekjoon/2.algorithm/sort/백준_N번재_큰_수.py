import sys

def solve():
    global nums

    nums.sort(reverse=True)
    print(nums[2])


t = int(sys.stdin.readline().strip())
for _ in range(t):
    nums = list(map(int, sys.stdin.readline().strip().split(" ")))
    solve()