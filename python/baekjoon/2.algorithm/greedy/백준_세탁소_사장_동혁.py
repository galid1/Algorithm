import sys

def solve():
    global nums

    for num in nums:
        # q 0.25
        q = num//25
        num %= 25

        # d 0.1
        d = num//10
        num %= 10

        # n 0.05
        n = num//5
        num %=5

        # p 0.01
        p = num//1
        num%=1

        print(q, d, n, p)


n = int(sys.stdin.readline().strip())
nums = []
for i in range(n):
    nums.append(int(sys.stdin.readline().strip()))
solve()