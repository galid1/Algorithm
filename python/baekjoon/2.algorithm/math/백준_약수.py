import sys

def solve():
    global ns
    ns.sort()

    if len(ns) == 1:
        print(pow(ns[0], 2))
        return

    print(ns[0] * ns[-1])



n = int(sys.stdin.readline().strip())
ns = list(map(int, sys.stdin.readline().strip().split(" ")))
solve()


# 1
# 2
# -> 4

# 3
# 2 4 8
# -> 16

# 1
# 5
# -> 25

# 7
# 2 3 4 6 9 12 18
# -> 36