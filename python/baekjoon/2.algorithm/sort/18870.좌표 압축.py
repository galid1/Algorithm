import sys


def solve():
    global n, cs

    cs.sort(key=lambda item: item[1])

    ans = [0 for _ in range(n)]
    cnt, idx = 0, 0
    while idx < n:
        position, coord = cs[idx]
        ans[position] = cnt

        jdx = idx+1
        while jdx < n:
            other_position, other_coord = cs[jdx]
            if other_coord != coord:
                break

            ans[other_position] = cnt
            jdx += 1

        same_cnt = jdx - idx
        cnt, idx = cnt + 1, idx + same_cnt

    print(*ans)


n = int(sys.stdin.readline().strip())
cs = list(map(int, sys.stdin.readline().strip().split(" ")))
for i in range(n):
    cs[i] = (i, cs[i])
solve()