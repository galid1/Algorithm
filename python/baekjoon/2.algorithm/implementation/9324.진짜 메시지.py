import sys
from collections import defaultdict


def solve(s):
    cnts = defaultdict(int)

    third = False
    for idx, c in enumerate(s):
        if third:
            third = False
            continue

        cnts[c] += 1

        if cnts[c] % 3 != 0:
            continue

        if idx + 1 >= len(s):
            return print("FAKE")

        if s[idx+1] != c:
            return print("FAKE")

        third = True

    print("OK")


n = int(sys.stdin.readline().strip())
for _ in range(n):
    solve(list(sys.stdin.readline().strip()))

# ABAACCC
# ABAAACCCC