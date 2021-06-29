import sys

def solution(cur, cur_sum, next_idx):
    global n, ans, visit, nums

    if len(cur) == n:
        if cur_sum not in visit.keys():
            ans += 1
            visit[cur_sum] = True
        return

    for i in range(next_idx, 4):
        cur += str(i)
        solution(cur, cur_sum + nums[i], i)
        cur = cur[:-1]

ans = 0
visit = {}
nums = {0: 1, 1: 5, 2: 10, 3: 50}
n = int(sys.stdin.readline())
solution('', 0, 0)
print(ans)