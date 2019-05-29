# 백준 11726

import sys

def tiling(n):
    if n < 3:
        return memo[n]

    for i in range(3, n+1):
        memo.append(memo[i-2] + memo[i-1])
    return memo[n]

memo = [0,1,2]
n = int(sys.stdin.readline())
print(tiling(n)%10007)