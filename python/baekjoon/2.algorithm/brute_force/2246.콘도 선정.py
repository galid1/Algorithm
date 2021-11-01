import sys


def solve():
    global n, cs

    ans = 0
    visited = [False for _ in range(n)]
    cs.sort(key=lambda item: item[1])
    for i in range(n):
        idx, cd, cc = cs[i]
        for j in range(i):
            jdx, td, tc = cs[j]
            if cd == td:
                break

            if cc >= tc:
                visited[idx] = True
                break

    cs.sort(key=lambda item: item[2])
    for i in range(n):
        idx, cd, cc = cs[i]

        if visited[idx]:
            continue

        for j in range(i):
            jdx, td, tc = cs[j]
            if cc == tc:
                break

            if cd >= td:
                visited[idx] = True
                break

    for v in visited:
        if not v:
            ans += 1
    print(ans)


n = int(sys.stdin.readline().strip())
cs = []
for i in range(n):
    cs.append([i] + list(map(int, sys.stdin.readline().strip().split(" "))))

solve()

# 6
# 1 3
# 1 4
# 2 3
# 2 5
# 3 3
# 5 2