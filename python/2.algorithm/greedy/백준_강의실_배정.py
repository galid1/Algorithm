import sys, heapq


def solve():
    global n, sts

    lectures = []
    l_cnt = 0

    ans = 0
    for s, t in sts:
        if not lectures:
            lectures.append((t, s))
            ans = 1
            l_cnt += 1
            continue

        while True:
            rt, rs = heapq.heappop(lectures)

            if s >= rt:
                l_cnt -= 1
                continue

            heapq.heappush(lectures, (rt, rs))
            heapq.heappush(lectures, (t, s))
            l_cnt += 1
            ans = max(ans, l_cnt)
            break

    print(ans)



n = int(sys.stdin.readline().strip())
sts = []
for _ in range(n):
    sts.append(list(map(int, sys.stdin.readline().strip().split(" "))))

sts.sort()
solve()


# 3
# 2 4
# 3 5
# 1 3