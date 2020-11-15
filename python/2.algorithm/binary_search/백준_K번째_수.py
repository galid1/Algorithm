import sys


def solution():
    global n, k

    s = 1
    e = k
    answer = 0
    while s <= e:
        mid = (s+e)//2

        smaller_sums = 0
        for i in range(1, n+1):
            smaller_sums += min(mid//i, n)

        if smaller_sums >= k:
            e = mid - 1
            answer = mid
        else:
            s = mid + 1

    print(answer)


n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
solution()