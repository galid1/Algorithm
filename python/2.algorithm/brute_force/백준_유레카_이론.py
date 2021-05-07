import sys


def solve():
    global k, ts

    for i in range(1, len(ts)):
        for j in range(1, len(ts)):
            for l in range(1, len(ts)):
                if ts[i]+ts[j]+ts[l] == k:
                    return print(1)
    print(0)


t = int(sys.stdin.readline().strip())
ts = []
for i in range(45):
    ts.append(i*(i+1)//2)

for _ in range(t):
    k = int(sys.stdin.readline().strip())
    solve()
