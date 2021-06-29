import sys

def solve():
    global n, m, nums, rs

    accumulated = [0]
    sums = 0
    for num in nums:
        sums += num
        accumulated.append(sums)

    for s, e in rs:
        print(accumulated[e] - accumulated[s-1])


n, m = map(int, sys.stdin.readline().strip().split(" "))
nums = list(map(int, sys.stdin.readline().strip().split(" ")))
rs = []
for _ in range(m):
    rs.append(tuple(map(int, sys.stdin.readline().strip().split(" "))))
solve()