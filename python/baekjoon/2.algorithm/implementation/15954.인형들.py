import sys, math


def solve():
    global n, k, prefs

    ans = sys.maxsize
    for start in range(n-k+1):
        for j in range(n-(k+start)+1):
            selected = prefs[start:start+k+j]
            sums = sum(selected)
            m = sums/len(selected)
            ans = min(ans, distribute(selected, m))

    print(math.sqrt(ans))


def distribute(selected, m):
    result = 0
    for pref in selected:
        result += pow((m - pref), 2)

    return result/len(selected)


n, k = map(int, sys.stdin.readline().strip().split(" "))
prefs = list(map(int, sys.stdin.readline().strip().split(" ")))

solve()
