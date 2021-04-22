import sys, heapq

def solve():
    global n, k, ss

    ss.sort()

    subs = []
    for i in range(1, n):
        sub = ss[i] - ss[i - 1]
        heapq.heappush(subs, -sub)

    for _ in range(k-1):
        if subs:
            heapq.heappop(subs)

    print(abs(sum(subs)))


n = int(sys.stdin.readline().strip())
k = int(sys.stdin.readline().strip())
ss = list(map(int, sys.stdin.readline().strip().split(" ")))
solve()

