import sys

def solve():
    global n, arr, ds

    for i in range(len(arr) - 1, -1, -1):
        ds[i] = 1

        for j in range(i+1, len(arr)):
            if arr[j] == arr[i]:
                ds[i] = max(ds[i], ds[j])
            elif arr[j] < arr[i]:
                ds[i] = max(ds[i], ds[j] + 1)

    print(max(ds))


n = int(sys.stdin.readline().strip())
ds = [0 for _ in range(n)]
ds[-1] = 1
arr = list(map(int, sys.stdin.readline().strip().split(" ")))

solve()