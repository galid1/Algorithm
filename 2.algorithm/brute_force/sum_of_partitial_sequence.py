# 백준 1182 부분수열의 합

import sys

def solution(sequence, m):
    result = [0]

    for i in range(len(sequence)):
        recusive(sequence, m, result, sequence[i], i+1)

    print(result[0])


def recusive(sequence, m, result, cur_sum, index):
    if cur_sum == m:
        result[0] += 1
    
    # 종료 조건
    if index > len(sequence):
        return

    for i in range(index, len(sequence)):
        recusive(sequence, m, result, cur_sum + sequence[i], i+1)



n, m = list(map(int, sys.stdin.readline().rstrip().split(" ")))
sequence = list(map(int, sys.stdin.readline().rstrip().split(" ")))
result = [0]
solution(sequence, m)
