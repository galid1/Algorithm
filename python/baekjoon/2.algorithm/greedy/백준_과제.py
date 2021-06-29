import sys

def solve():
    global n, dws

    dws.sort(reverse=True)

    scores = [0 for _ in range(1001)]

    for w, d in dws:
        for i in range(d, 0, -1):
            if not scores[i]:
                scores[i] = w
                break

    print(sum(scores))


n = int(sys.stdin.readline().strip())
dws = []
for _ in range(n):
    d, w = map(int, sys.stdin.readline().strip().split(" "))
    dws.append((w, d))

solve()