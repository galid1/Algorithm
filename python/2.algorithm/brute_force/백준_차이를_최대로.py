import sys, itertools

def solution(arr):
    ps = list(itertools.permutations(arr))

    max_num = 0

    for p in ps:
        sums = 0
        for j in range(0, len(p)-1):
            sums += abs(p[j] - p[j+1])

        max_num = max(max_num, sums)

    print(max_num)


n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split(" ")))
solution(arr)