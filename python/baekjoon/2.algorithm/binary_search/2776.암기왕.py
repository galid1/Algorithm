import sys


def solve(n, ns, m, ms):
    ns.sort()

    for num in ms:
        s, e = 0, n-1
        answered = False

        while e >= s:
            m = (s+e)//2

            if ns[m] == num:
                answered = True
                print(1)
                break
            elif ns[m] > num:
                e = m-1
            else:
                s = m+1

        if not answered:
            print(0)


t = int(sys.stdin.readline().strip())
for _ in range(t):
    n = int(sys.stdin.readline().strip())
    ns = list(map(int, sys.stdin.readline().strip().split(" ")))
    m = int(sys.stdin.readline().strip())
    ms = list(map(int, sys.stdin.readline().strip().split(" ")))
    solve(n, ns, m, ms)