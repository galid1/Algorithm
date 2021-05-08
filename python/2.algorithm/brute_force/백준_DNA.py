import sys


def solve():
    global n, m, dnas

    res = ''
    for i in range(m):
        ds = {chr(i): 0 for i in range(ord('A'), ord('Z') + 1)}
        for j in range(n):
            ds[dnas[j][i]] += 1

        max_c = ''
        max_cnt = 0
        for k in range(ord('A'), ord('Z') + 1):
            if ds[chr(k)] > max_cnt:
                max_cnt = ds[chr(k)]
                max_c = chr(k)
        res += max_c

    hd = 0
    for i in range(m):
        for j in range(n):
            if res[i] != dnas[j][i]:
                hd += 1
    print(res)
    print(hd)


n, m = map(int, sys.stdin.readline().strip().split(" "))
dnas = []
for _ in range(n):
    dnas.append(sys.stdin.readline().strip())
solve()

# print(ord('A')) == 65
