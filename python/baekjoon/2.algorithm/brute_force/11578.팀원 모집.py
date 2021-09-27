import sys


def solve():
    global n, m, stds, ans

    for pop_cnt in range(1, m+1):
        if ans < 11:
            return

        problems = set([i for i in range(1, n+1)])
        print("================== cnt : ", pop_cnt)
        dfs(pop_cnt, 0, problems, 0)


def dfs(pop_cnt, cnt, problems, start_idx):
    global ans, stds

    if ans < 11:
        return

    if pop_cnt == cnt:
        if not problems:
            print(problems, cnt)
            ans = cnt
        return

    for std_idx in range(start_idx, m):
        dfs(pop_cnt, cnt+1, problems.difference(stds[std_idx]), std_idx + 1)

    # for std_idx in range(start_idx, m):
    #     problems.difference_update(stds[std_idx])
    #     dfs(pop_cnt, cnt+1, problems.difference(stds[std_idx]), std_idx + 1)
    #     problems.update(stds[std_idx]) # <= 다시 추가하는 상황에서 이전의 학생이 3,4 였고 두번전의 학생이 4였다면, 되돌리는 상황에서 4가 누락됨


n, m = map(int, sys.stdin.readline().strip().split(" "))
stds = []
for _ in range(m):
    stds.append(list(map(int, sys.stdin.readline().strip().split(" ")))[1:])

ans = 11
solve()

if ans == 11:
    print(-1)
else:
    print(ans)


# 10 10
# 1 10
# 1 4
# 2 3 4
# 3 1 2 4
# 5 1 2 3
# 4 1 2 9
# 3 6 7 8
# 4 9 3 2 1
# 3 3 4 5
# 5 7 9 1 2 3