import sys

def solve():
    global n, k

    d = [[] for _ in range(11)]
    d[1].append('1')
    d[2].append('1+1')
    d[2].append('2')
    d[3].append('1+1+1')
    d[3].append('1+2')
    d[3].append('2+1')
    d[3].append('3')

    for i in range(4, n+1):
        for exp in d[i-1]:
            d[i].append('1+'+exp)
        for exp in d[i-2]:
            d[i].append('2+'+exp)
        for exp in d[i-3]:
            d[i].append('3+'+exp)

    if k-1 >= len(d[n]):
        print(-1)
    else:
        print(d[n][k-1])


n, k = map(int, sys.stdin.readline().strip().split(" "))
solve()