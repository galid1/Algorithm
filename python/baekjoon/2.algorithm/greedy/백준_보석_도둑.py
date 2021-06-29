import sys, heapq

def solve():
    global n, k, mvs, cs

    ans = 0
    mvs = sorted(mvs, key=lambda mvs: mvs[0])
    cs.sort()
    prio_q = []

    for c in cs:
        while mvs and c >= mvs[0][0]:
            v = heapq.heappop(mvs)[1]
            heapq.heappush(prio_q, -v)

        if prio_q:
            ans += heapq.heappop(prio_q)

    print(-ans)


n, k = map(int, sys.stdin.readline().strip().split(" "))
mvs, cs = [], []
for i in range(n):
    mv = tuple(map(int, sys.stdin.readline().strip().split(" ")))
    mvs.append(mv)

for j in range(k):
    cs.append(int(sys.stdin.readline().strip()))

solve()

# 4 4
# 3 1
# 4 1
# 5 1
# 6 1
# 3
# 4
# 2
# 1
