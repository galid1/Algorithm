# 백준 2156 포도주 시식
# d[i][j] = i번째 포도주 까지 고려했을 때 j번 연속으로 마셨을 때의 최댓값

import sys

def grape_taste(n):
    # 초기화
    d[0][0] = 0
    d[0][1] = G[0]
    d[0][2] = G[0]

    # 연산
    for i in range(1, n):
        d[i][0] = max(d[i-1][0], d[i-1][1], d[i-1][2])
        d[i][1] = d[i-1][0] + G[i]
        d[i][2] = d[i-1][1] + G[i]

    print(max(d[n-1][0], d[n-1][1], d[n-1][2]))


d = [[0 for i in range(3)] for i in range(10001)]
n = int(sys.stdin.readline())
G = []
for i in range(n):
    G.append(int(sys.stdin.readline()))
grape_taste(n)