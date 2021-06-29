import sys


def solution():
    global arr
    answer = 0

    start = 0
    for a in arr:
        if a[0] >= start:
            answer += 1
            start = a[1]

    print(answer)


n = int(sys.stdin.readline())
arr = []
for i in range(n):
    arr.append(list(map(int, sys.stdin.readline().strip().split(" "))))

arr.sort(key = lambda v: (v[1], v[0]))

solution()
