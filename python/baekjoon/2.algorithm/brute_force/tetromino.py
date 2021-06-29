# baekjoon 14500 테트로미노

import sys

n, m = map(int , sys.stdin.readline().split(" "))
f = []
for i in range(n):
    f.append(list(map(int, sys.stdin.readline().strip().split(" "))))


max_num = 0

for i in range(n):
    for j in range(m):
        if j + 3 < m:
            # ㅡ
            max_num = max(max_num, f[i][j] + f[i][j+1] + f[i][j+2] + f[i][j+3])

        if i + 3 < n:
            # ㅣ
            max_num = max(max_num, f[i][j] + f[i+1][j] + f[i+2][j] + f[i+3][j])

        if j + 1 < m and i + 1 < n:
            # ㅁ
            max_num = max(max_num, f[i][j] + f[i][j+1] + f[i+1][j] + f[i+1][j+1])

        if j + 1 < m and i + 2 < n:
            max_num = max(max_num, f[i][j] + f[i+1][j] + f[i+2][j] + f[i+2][j+1])
            max_num = max(max_num, f[i][j] + f[i][j+1] + f[i+1][j+1] + f[i+2][j+1])
            max_num = max(max_num, f[i][j] + f[i+1][j] + f[i+2][j] + f[i][j+1])
            max_num = max(max_num, f[i][j+1] + f[i+1][j+1] + f[i+2][j] + f[i+2][j+1])

        if j + 2 < m and i + 1 < n:
            max_num = max(max_num, f[i][j] + f[i][j+1] + f[i][j+2] + f[i+1][j])
            max_num = max(max_num, f[i][j+2] + f[i+1][j] + f[i+1][j+1] + f[i+1][j+2])
            max_num = max(max_num, f[i][j] + f[i+1][j] + f[i+1][j+1] + f[i+1][j+2])
            max_num = max(max_num, f[i][j] + f[i][j+1] + f[i][j+2] + f[i+1][j+2])

        if j + 2 < m and i + 1 < n :
            max_num = max(max_num, f[i][j] + f[i][j+1] + f[i+1][j+1] + f[i+1][j+2])
            max_num = max(max_num, f[i+1][j] + f[i][j+1] + f[i+1][j+1] + f[i][j+2])
            # ㅗ ㅜ
            max_num = max(max_num, f[i][j+1] + f[i+1][j] + f[i+1][j+1] + f[i+1][j+2])
            max_num = max(max_num, f[i][j] + f[i][j+1] + f[i][j+2] + f[i+1][j+1])

        if j + 1 < m and i + 2 < n :
            max_num = max(max_num, f[i][j+1] + f[i+1][j] + f[i+1][j+1] + f[i+2][j])
            max_num = max(max_num, f[i][j] + f[i+1][j] + f[i+1][j+1] + f[i+2][j+1])
            # ㅓ ㅏ
            max_num = max(max_num, f[i+1][j] + f[i][j+1] + f[i+1][j+1] + f[i+2][j+1])
            max_num = max(max_num, f[i][j] + f[i+1][j] + f[i+1][j+1] + f[i+2][j])

print(max_num)