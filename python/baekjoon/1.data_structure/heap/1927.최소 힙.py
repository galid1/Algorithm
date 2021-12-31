import heapq
import sys
input = sys.stdin.readline

t = int(input())
heap = []

for _ in range(t):
    cmd = int(input())

    if cmd == 0:
        try:
            print(heapq.heappop(heap))
        except:
            print(0)
    else:
        heapq.heappush(heap, cmd)