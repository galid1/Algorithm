import sys
from collections import deque

def solve():
    global a, b

    q = deque()
    q.append(a)

    ans = 0
    while q:
        ans += 1
        for i in range(len(q)):
            cur = q.popleft()

            if cur == b:
                print(ans)
                return

            if cur*2 <= b:
                q.append(cur*2)
            if len(str(cur)) < len(str(b)):
                q.append(int(str(cur) + '1'))
            if int(str(cur)+'1') == b:
                q.append(int(str(cur)+'1'))

    print(-1)


a, b = map(int, sys.stdin.readline().strip().split(" "))
solve()