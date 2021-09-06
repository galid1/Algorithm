import sys


def solve(cur, ck):
    global n, k, length, ans, visited

    cur_num = int(''.join(cur))

    if len(str(cur_num)) < length:
        return

    if ck == k:
        ans = max(ans, cur_num)
        return

    if cur_num in visited[ck]:
        return

    visited[ck].add(cur_num)

    for i in range(length):
        for j in range(length):
            if i == j:
                continue

            cur[i], cur[j] = cur[j], cur[i]
            solve(cur, ck+1)
            cur[i], cur[j] = cur[j], cur[i]


n, k = map(int, sys.stdin.readline().strip().split(" "))
listed_n = list(str(n))
length = len(listed_n)

visited = [set() for _ in range(k)]
ans = 0
solve(listed_n, 0)


if ans == 0:
    print(-1)
else:
    print(ans)