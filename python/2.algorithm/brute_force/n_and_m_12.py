# 백준 15665 n과 m 11

import sys

def solution(r = 0, result_arr = []):
    global n, m, nums, visit_result

    if r >= m :
        result = ""
        for num in result_arr:
            result += str(num) + " "

        if result in visit_result:
            return

        visit_result.add(result)
        print(result)
        return

    for num in nums:
        tmp = result_arr.copy()
        tmp.append(num)
        solution(r + 1, tmp)


n, m = map(int, sys.stdin.readline().rstrip().split(" "))
nums = list(map(int, sys.stdin.readline().rstrip().split(" ")))
nums.sort()
visit_result = set()
solution()
