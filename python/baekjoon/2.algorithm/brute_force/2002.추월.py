import sys


def solve():
    global n, ins, outs

    ans = 0

    for out_car in outs:
        if ins[0] != out_car:
            ans += 1

        del ins[ins.index(out_car)]

    print(ans)


n = int(sys.stdin.readline().strip())
ins = []
for _ in range(n):
    ins.append(sys.stdin.readline().strip())

outs = []
for _ in range(n):
    outs.append(sys.stdin.readline().strip())

solve()
