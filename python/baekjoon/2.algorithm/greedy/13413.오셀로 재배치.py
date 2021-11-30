import sys


def solve():
    global n, origin, target

    need_b, need_w = 0, 0
    for i in range(n):
        if target[i] != origin[i]:
            if target[i] == 'W':
                need_w += 1
            else:
                need_b += 1

    switching_cnt = min(need_b, need_w)
    change_cnt = max(need_b, need_w) - switching_cnt

    print(switching_cnt + change_cnt)


t = int(sys.stdin.readline().strip())
for _ in range(t):
    n = int(sys.stdin.readline().strip())
    origin = list(sys.stdin.readline().strip())
    target = list(sys.stdin.readline().strip())
    solve()