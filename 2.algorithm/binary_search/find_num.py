# 백준 1920 수 찾기

import sys

def solution(n_nums, m_nums):
    n_nums.sort()
    result = [0 for i in range(len(m_nums))]

    start = 0
    end = len(n_nums)

    for i in range(len(m_nums)):
        start = 0
        end = len(n_nums)

        while (end - start) >= 0:
            mid = (start + end) // 2

            if mid >= len(n_nums) or mid < 0:
                break

            if m_nums[i] == n_nums[mid]:
                result[i] = 1
                break
            elif m_nums[i] < n_nums[mid]:
                end = mid - 1
            else:
                start = mid + 1

    # 결과 출력
    for num in result:
        print(num)


n = int(sys.stdin.readline())
n_nums = list(map(int, sys.stdin.readline().rstrip().split(" ")))
m = int(sys.stdin.readline())
m_nums = list(map(int, sys.stdin.readline().rstrip().split(" ")))
solution(n_nums, m_nums)