import sys
import heapq

def solve():
    global cards

    ans = 0

    while len(cards) > 1:
        new_deck = heapq.heappop(cards) + heapq.heappop(cards)
        ans += new_deck
        heapq.heappush(cards, new_deck)

    print(ans)


n = int(sys.stdin.readline().strip())
cards = []
for i in range(n):
    heapq.heappush(cards, int(sys.stdin.readline()))
solve()