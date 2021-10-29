import sys


def solve():
    global n, fs

    ans = 0

    for i in range(n):
        visited = set()
        for j in range(n):
            if fs[i][j] == 'Y':
                visited.add(j)

                for k in range(n):
                    if fs[j][k] == 'Y':
                        visited.add(k)

        ans = max(ans, len(visited)-1)

    print(ans)


n = int(sys.stdin.readline().strip())
fs = []
for _ in range(n):
    fs.append(list(sys.stdin.readline().strip()))

solve()