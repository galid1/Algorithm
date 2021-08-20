import sys


def solve(target, rings):
    ans = 0
    for ring in rings:
        if (is_include(ring, target)):
            ans += 1

    print(ans)


def is_include(ring, target):
    for i in range(len(ring)):
        include = True
        for j, c in enumerate(target):
            if ring[(i+j)%len(ring)] != c:
                include = False
                break

        if include:
            return True

    return False



target = sys.stdin.readline().strip()
n = int(sys.stdin.readline().strip())
rings = []
for _ in range(n):
    rings.append(sys.stdin.readline().strip())

solve(target, rings)