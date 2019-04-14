# 백준 11057 오르막수

import sys

def uphill_road_num(n):
    result = 0
   
    # n = 1 일때 초기화
    for i in range(10):
        d[1][i] = 1
    
    # 이미 존재   
    if d[n][0] > 0:
        for j in range(10):
            result += (d[n][j])%10007
        print(result)
        return

    # n >= 2 d[k][h]
    for k in range(2, n+1):
        for g in range(10):
            for h in range(g+1):
                d[k][g] += (d[k - 1][h])%10007

    # 값구하기
    for m in range(10):
        result += (d[n][m])%10007
    print(result%10007)
    
    

d = [[0 for i in range(10)] for i in range(1001)]
n = int(sys.stdin.readline())
uphill_road_num(n)
