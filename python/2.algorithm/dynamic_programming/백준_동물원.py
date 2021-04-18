import sys

def solve():
    global n

    d = [[0 for _ in range(3)] for _ in range(2)]
    d[1][0] = 1
    d[1][1] = 1
    d[1][2] = 1

    for i in range(2, n+1):
        ni = i%2
        bi = 0 if ni == 1 else 1
        d[ni][0] = d[bi][0] + d[bi][1] + d[bi][2]
        d[ni][1] = d[bi][0] + d[bi][2]
        d[ni][2] = d[bi][0] + d[bi][1]

    print(sum(d[n%2])%9901)


n = int(sys.stdin.readline().strip())
solve()