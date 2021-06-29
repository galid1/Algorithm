import sys, heapq


def solve():
    global n, m, cards

    heapq.heapify(cards)

    for _ in range(m):
        x = heapq.heappop(cards)
        y = heapq.heappop(cards)

        heapq.heappush(cards, x+y)
        heapq.heappush(cards, x+y)

    print(sum(cards))




n, m = map(int, sys.stdin.readline().strip().split(" "))
cards = list(map(int, sys.stdin.readline().strip().split(" ")))
solve()

# 3 1
# 3 2 6