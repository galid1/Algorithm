import sys, heapq


def solve():
    global n, cards

    ans = 0

    while len(cards) > 1:
        a, b = heapq.heappop(cards), heapq.heappop(cards)
        sums = a + b

        ans += sums

        heapq.heappush(cards, sums)

    print(ans)


n = int(sys.stdin.readline().strip())
cards = []
for _ in range(n):
    heapq.heappush(cards, int(sys.stdin.readline().strip()))

solve()