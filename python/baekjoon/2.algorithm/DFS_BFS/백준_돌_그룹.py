import sys
from collections import deque

# *** 1 <= a,b,c <= 500 조건은, 주어진 a,b,c의 조건일 뿐이지, 중간중간 계산 결과로 나온 값은 500을 넘어도 되고, 1보다 작아도 된다.

def solve():
    global a, b, c

    stones = (a, b, c)

    visited = set(stones)
    q = deque([stones])

    while q:
        a, b, c = q.popleft()

        for x, y, z in ((a, b, c), (b, c, a), (a, c, b)):
            if x == y == z:
                return print(1)

            if x == y:
                continue

            if x > y:
                x, y = y, x

            y -= x
            x += x

            if (x, y, z) in visited:
                continue

            q.append((x, y, z))
            visited.add((x, y, z))

    print(0)


ds = [(0, 1, 2), (0, 2, 1), (1, 2, 0)]
a, b, c = map(int, sys.stdin.readline().strip().split(" "))
solve()
