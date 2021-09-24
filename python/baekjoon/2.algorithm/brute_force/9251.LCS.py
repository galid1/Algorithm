import sys


def solve():
    global s1, s2

    d = [[0 for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]


    for i in range(1, len(s1)+1):
        for j in range(1, len(s2)+1):
            if s1[i-1] == s2[j-1]:
                d[i][j] = d[i-1][j-1] + 1
                continue

            d[i][j] = max(d[i-1][j], d[i][j-1])

    for dd in d:
        print(dd)

    print(d[len(s1)][len(s2)])


s1 = sys.stdin.readline().strip()
s2 = sys.stdin.readline().strip()

solve()

# ababab
# abbaba