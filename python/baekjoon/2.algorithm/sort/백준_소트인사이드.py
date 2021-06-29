import sys

def solution(arr):
    for i in range(len(arr) - 1):
        max_idx = i
        for j in range(i+1, len(arr)):
            if arr[max_idx] < arr[j]:
                max_idx = j
        arr[max_idx], arr[i] = arr[i], arr[max_idx]

    for n in arr:
        print(n, end='')


arr = list(map(int, list(sys.stdin.readline().strip())))
solution(arr)