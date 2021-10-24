import sys


def solve():
    global n, k, arr

    ans = 0
    visited = [False for _ in range(n)]
    for idx, t in enumerate(arr):
        if t == "P":
            visited[idx] = True

    for idx, t in enumerate(arr):
        if t == "H":
            continue

        for i in range(max(idx-k, 0), min(idx+k+1, n)):
            if not visited[i]:
                visited[i] = True
                ans += 1
                break

    print(ans)


n, k = map(int, sys.stdin.readline().strip().split(" "))
arr = list(sys.stdin.readline().strip())
solve()

# 20 1
# HHPHPPHHPPHPPPHPHPHP