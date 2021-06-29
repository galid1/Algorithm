import sys

def solve():
    global n, dps

    dps.sort(key=lambda item: item[0])
    days = [0 for _ in range(10001)]

    while dps:
        pay, deadline = dps.pop()

        for i in range(deadline, 0, -1):
            if not days[i]:
                days[i] = pay
                break

    print(sum(days))



n = int(sys.stdin.readline().strip())
dps = []
for _ in range(n):
    dps.append(list(map(int, sys.stdin.readline().strip().split(" "))))
solve()
