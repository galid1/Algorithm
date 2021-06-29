import sys

def  solution():
    n = int(sys.stdin.readline())
    arr = []
    for i in range(n):
        arr.append(list(map(int, sys.stdin.readline().split(" "))))

    arr.sort(key=lambda a: a[0])

    ans = 0
    min_interview = 100001
    for a in arr:
        if a[1] < min_interview:
            ans += 1
            min_interview = a[1]
    print(ans)


t = int(sys.stdin.readline())
for i in range(t):
    solution()