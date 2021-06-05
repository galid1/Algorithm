import sys


def solve():
    global n, k

    visited = [False for _ in range(n+1)]

    idx = 0

    # 제일 작은 소수 선택
    for cur_num in range(2, n+1):
        if visited[cur_num]:
            continue

        cur_mul = 0
        while cur_mul + cur_num <= n and idx < k:
            cur_mul += cur_num

            if visited[cur_mul]:
                continue
            idx += 1
            visited[cur_mul] = True

        if idx == k:
            return print(cur_mul)


n, k = map(int, sys.stdin.readline().strip().split(" "))
solve()