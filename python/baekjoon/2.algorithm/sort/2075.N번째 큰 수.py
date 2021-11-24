import sys, heapq


n = int(sys.stdin.readline().strip())
nums = []

need_pop_cnt = n * n - n
cur_pop_cnt = 0
for _ in range(n):
    line = list(map(int, sys.stdin.readline().strip().split(" ")))

    for num in line:
        heapq.heappush(nums, num)

    if len(nums) < n:
        continue

    while len(nums) > n:
        heapq.heappop(nums)
        cur_pop_cnt += 1

    if cur_pop_cnt == need_pop_cnt:
        break

print(heapq.heappop(nums))
