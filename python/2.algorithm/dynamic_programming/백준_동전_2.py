import sys

def solution():
    global d, n, k, cs

    for i in range(1, n + 1):
        for j in range(1, k+1):
            if j < cs[i]:
                d[i][j] = d[i-1][j]
            else:
                if d[i-1][j] == -1 and d[i][j-cs[i]] == -1:
                    d[i][j] = -1
                elif d[i-1][j] != -1 and d[i][j-cs[i]] != -1:
                    d[i][j] = min(d[i-1][j], 1 + d[i][j-cs[i]])
                else:
                    d[i][j] = max(d[i - 1][j], 1 + d[i][j - cs[i]])


n, k = map(int, sys.stdin.readline().strip().split(" "))
d = [[0 for _ in range(k+1)] for _ in range(n+1)]
for i in range(1, k+1):
    d[0][i] = -1
cs = [0]
for i in range(n):
    cs.append(int(sys.stdin.readline()))
cs.sort()

solution()
print(d[n][k])
