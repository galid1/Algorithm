# baekjoon 10815 숫자 카드

import sys

def solution(n_arr, m_arr):
    n_arr.sort()
    result = [0 for i in range(len(m_arr))]

    for i in range(len(m_arr)):
        start = 0
        end = len(n_arr) - 1

        while (end - start) >= 0 and (end - start)//2 < len(n_arr):
            mid = (start + end) // 2

            if m_arr[i] == n_arr[mid]:
                result[i] = 1
                break

            elif m_arr[i] < n_arr[mid]:
                end = mid - 1

            else :
                start = mid + 1

    for j in range(len(result)):
        print(result[j])


n = int(sys.stdin.readline())
n_arr = list(map(int, sys.stdin.readline().rstrip().split(" ")))
m = int(sys.stdin.readline())
m_arr = list(map(int, sys.stdin.readline().rstrip().split(" ")))

solution(n_arr, m_arr)