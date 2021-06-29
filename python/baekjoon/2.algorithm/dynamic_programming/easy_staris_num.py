# baekjoon 10844 쉬운 계단 수

import sys

def easy_stairs_num(n):
    # n = 1일때
    for i in range(1,10):
        d[1][i] = 1
    # n = 2일때 , n = 3일때 맨마지막 수가 1인경우 0,2 가 올수있는게 다르므로 따로 처리
    for j in range(0,10):
        if j == 0:
            d[2][j] = d[1][1]
            continue
        if j == 1:
            d[2][j] = d[1][2]
        if j == 9:
            d[2][j] = d[1][8]
            continue
        d[2][j] = d[1][j - 1] + d[1][j + 1]

    # n >= 3 맨 마지막수가 1일때 0, 2 가 올 수 있음
    for k in range(3, n+1):
        for h in range(0, 10):
            if h == 0:
                d[k][h] = (d[k - 1][1])%1000000000
                continue
            if h == 9:
                d[k][h] = (d[k - 1][8])%1000000000
                continue
            d[k][h] = (d[k - 1][h - 1] + d[k - 1][h + 1])%1000000000

    result = 0
    for g in range(0,10):
        result += d[n][g]
    print((result)%1000000000)

d = [[0 for i in range(10)] for i in range(101)]
n = int(sys.stdin.readline())
easy_stairs_num(n)