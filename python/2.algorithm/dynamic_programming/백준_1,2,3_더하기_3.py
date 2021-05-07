import sys

d = [0 for _ in range(1000001)]
d[1] = 1
d[2] = 2
d[3] = 4
m = 1000000009
for i in range(4, 1000001):
    d[i] = (d[i-1] % m) + (d[i-2] % m) + (d[i-3] % m)

t = int(sys.stdin.readline().strip())
for _ in range(t):
    num = int(sys.stdin.readline().strip())
    print((d[num]) % m)