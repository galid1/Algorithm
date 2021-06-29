# baekjoon 15657 n과 m 8

import sys

def solution(r = 0, result_arr = []):
    global n, m, nums

    if r >= m :
        result = ''
        for num in result_arr:
            result += str(num) + ' '
        print(result)
        return

    for num in nums:
        if r > 0 and result_arr[r - 1] > num:
            continue
        tmp = result_arr.copy()
        tmp.append(num)
        solution(r + 1, tmp)


n, m = map(int, sys.stdin.readline().rstrip().split(" "))
nums = list(map(int, sys.stdin.readline().rstrip().split(" ")))
nums.sort()
solution()
