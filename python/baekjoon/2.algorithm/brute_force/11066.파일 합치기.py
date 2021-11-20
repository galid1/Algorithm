import sys, heapq


def solve():
    global n, files

    heapq.heapify(files)

    ans = 0
    while files:
        f1 = heapq.heappop(files)
        if not files:
            break

        f2 = heapq.heappop(files)

        cost = f1 + f2
        ans += cost
        heapq.heappush(files, cost)

    print(ans)


t = int(sys.stdin.readline().strip())
for _ in range(t):
    n = int(sys.stdin.readline().strip())
    files = list(map(int, sys.stdin.readline().strip().split(" ")))
    solve()

# 15
# 1 21 3 4 5 35 5 4 3 5 98 21 14 17 32