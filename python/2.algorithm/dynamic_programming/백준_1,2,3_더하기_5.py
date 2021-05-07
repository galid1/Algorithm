import sys


t = int(sys.stdin.readline().strip())
# Check, 1, 2, 3
d = [[0, 0, 0, 0] for _ in range(100001)]
d[1][1] = 1
d[2][2] = 1
d[3][1] = 1
d[3][2] = 1
d[3][3] = 1

m = 1000000009
for i in range(4, 100001):
    # 1000000009 으로 나눈 나머지를 저장
    # 1 + n-1[2, 3]
    d[i][1] = (d[i - 1][2] + d[i - 1][3]) % m
    # 2 + n-2[1, 3]
    d[i][2] = (d[i - 2][1] + d[i - 2][3]) % m
    # 3 + n-3[1, 2]
    d[i][3] = (d[i - 3][1] + d[i - 3][2]) % m

for _ in range(t):
    num = int(sys.stdin.readline().strip())
    print(sum(d[num]) % 1000000009)
