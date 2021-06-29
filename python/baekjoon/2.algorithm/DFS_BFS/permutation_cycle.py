# baekjoon 10451 순열사이클

import sys

def solve(path):
    visit = [0 for k in range(1001)]
    count = 0

    for i in range(1, len(path)):
        if not visit[i]:
            count += 1
            dfs(path, visit, i)

    return count


def dfs(path, visit, start):
    stack = [start]
    visit[start] = True

    while stack:
        cur = stack.pop()
        next = path[cur]

        if next == start:
            return

        visit[next] = True
        stack.append(next)


t_list = []
t = int(sys.stdin.readline())
for i in range(t):
    t_num = int(sys.stdin.readline())
    t_case = [0] + list(map(int, sys.stdin.readline().split(" ")))
    t_list.append(t_case)

for arr in t_list:
    print(solve(arr))

