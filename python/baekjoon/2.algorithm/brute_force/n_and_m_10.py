# baekjoon 15656 n과 m 9

import sys

def solution(r = 0, result_arr = []):
    global n, m, nums, visit, visit_result

    if r >= m :
        result = ''
        for num in result_arr:
            result += str(num) + ' '

        if result in visit_result:
            return

        visit_result.add(result)
        print(result)
        return

    for i in range(n):
        if visit[i]:
            continue

        tmp = result_arr.copy()
        tmp.append(nums[i])
        visit[i] = True
        solution(r + 1, tmp)
        visit[i] = False

n, m = map(int, sys.stdin.readline().rstrip().split(" "))
nums = list(map(int, sys.stdin.readline().rstrip().split(" ")))
visit = [False for i in range(n)]
visit_result = set()
nums.sort()
solution()
