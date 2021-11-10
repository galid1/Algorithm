import sys, heapq

def solve():
    global n, k, arr

    arr.sort()

    subs = []
    for i in range(n-1):
        heapq.heappush(subs, arr[i+1] - arr[i])


    ans = 0
    for _ in range(n-k):
        ans += abs(heapq.heappop(subs))

    print(ans)



n, k = map(int, sys.stdin.readline().strip().split(" "))
arr = list(map(int, sys.stdin.readline().strip().split(" ")))
solve()
