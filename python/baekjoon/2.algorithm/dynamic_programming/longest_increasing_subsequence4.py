#baekjoon 14002 가장 긴 증가하는 부분 수열 4

import sys
import collections

def longest_increasing_subsequence4(arr):
    d = [0 for i in range(len(arr))]
    v = [0 for i in range(len(arr))]

    d[1] = 1
    for i in range(2, len(arr)):
        for j in range(i-1, -1, -1):
            if arr[j] >= arr[i]:
                continue
            if d[j] + 1 > d[i] :
                d[i] = d[j] + 1
                v[i] = j

    result = []
    max_num = -1
    max_num_index = -1
    # 최대 길이와 그 길이를 가진 인덱스 구하기
    for k in range(1, len(arr)):
        if d[k] > max_num :
            max_num = d[k]
            max_num_index = k

    # 수열을 result에 담기
    while v[max_num_index] != 0:
        result.append(arr[max_num_index])
        max_num_index = v[max_num_index]
    result.append(arr[max_num_index])
    result.reverse()

    print(max(d))
    for g in result:
        print(g, end=" ")


n = int(sys.stdin.readline())
arr = collections.deque(list(map(int, sys.stdin.readline().rstrip().split(" "))))
arr.appendleft(0)
longest_increasing_subsequence4(arr)
