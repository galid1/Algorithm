# 백준 2583 영역 구하기

import sys

def getting_area(matrix, blocks):
    # block 영역 처리
    for block in blocks:
        for i in range(block[0], block[2]):
            for j in range(block[1], block[3]):
                print(i, j)


m, n, k = map(int, sys.stdin.readline().rstrip().split(" "))
matrix = [[0 for i in range(n+1)] for i in range(m+1)]
blocks = []
for i in range(k):
    blocks.append(list(map(int, sys.stdin.readline().rstrip().split(" "))))
getting_area(matrix, blocks)
