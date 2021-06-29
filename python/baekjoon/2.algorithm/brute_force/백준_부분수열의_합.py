import sys


def solve(cnt, cur, start_idx, selected_cnt):
    global n, nums, visited

    if selected_cnt == cnt:
        visited.add(cur)
        return

    for i in range(start_idx, n):
        solve(cnt, cur+nums[i], i+1, selected_cnt+1)


n = int(sys.stdin.readline().strip())
nums = list(map(int, sys.stdin.readline().strip().split(" ")))
visited = set()

for i in range(1, n+1):
    solve(i, 0, 0, 0)

visited = sorted(visited)
num = 1
for exist_num in visited:
    if num != exist_num:
        print(num)
        exit()
    num += 1

print(num)