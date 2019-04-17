# 백준 2193번 이친수
# n = 1인 경우 => 1만 됨 (0으로 시작 X)
# n = 2인 경우 => 10 만됨 (11 X)
# n = 3인 경우 => 1. 3번째 자리에 `0`이 오는 경우 그 전 자리에 1이 올 수도 있고 0이 올 수도 있음.
#                 2. 3번째 자리에 `1`이 오는 경우 그 전 자리에 0만 올 수 있음.
#                 위의 2가지 경우를 합치면 n이 3인 경우의 n자리의 이친수 개수를 구할 수 있음

import sys

def specific_binary_num(n):
    d[1][0] = 0
    d[1][1] = 1
    d[2][0] = 1
    d[2][1] = 0

    for i in range(3, n+1):
        d[i][0] = d[i-1][0] + d[i-1][1]
        d[i][1] = d[i-1][0]

    print(d[n][0] + d[n][1])

d = [ [0,0] for i in range(91) ]
n = int(sys.stdin.readline())
specific_binary_num(n)