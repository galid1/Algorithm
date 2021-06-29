import sys

def solve():
    global n

    d = [0 for _ in range(n+1)]

    for i in range(1, n+1):
        min_num = sys.maxsize

        for j in range(1, 100000):
            if j**2 > i:
                break
            min_num = min(min_num, d[i-j**2]+1)
        d[i] = min_num

    print(d[n])

n = int(sys.stdin.readline().strip())
solve()
