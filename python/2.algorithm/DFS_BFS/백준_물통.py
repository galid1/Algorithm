import sys
from collections import deque


def solve():
    global os, a, b, c, ds
    # 정답
    ans = set()

    # a, b, c
    visited = [[[False for _ in range(201)] for _ in range(201)] for _ in range(201)]

    q = deque([(0, 0, c)])
    visited[0][0][c] = True
    ans.add(c)

    while q:
        wa, wb, wc = q.popleft()

        for f, t in ds:
            waters = [wa, wb, wc]

            # 옮기려는 물의 양이 0인 경우 건너 띔
            if waters[f] == 0:
                continue

            # will_move_water = min(waters[f], os[t]-waters[t])
            # waters[f] -= will_move_water
            # waters[t] += will_move_water
            after_t_water = min(waters[f]+waters[t], os[t])
            after_f_water = waters[f] - (after_t_water - waters[t])
            waters[f], waters[t] = after_f_water, after_t_water

            if not visited[waters[0]][waters[1]][waters[2]]:
                visited[waters[0]][waters[1]][waters[2]] = True
                q.append((waters[0], waters[1], waters[2]))
                if waters[0] == 0:
                    ans.add(waters[2])

    ans = list(ans)
    ans.sort()
    print(*ans)


ds = [(0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1)]
a, b, c = map(int, sys.stdin.readline().strip().split(" "))
# 원래 물통의 크기
os = [a, b, c]

solve()
