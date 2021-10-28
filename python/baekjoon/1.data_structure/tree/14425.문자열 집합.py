import sys


def solve():
    global n, m, ns, ms

    trie = make_trie(ns)

    ans = 0
    for st in ms:
        c_trie = trie
        exist = True
        for idx, c in enumerate(st):
            if c not in c_trie[0].keys():
                exist = False
                break

            c_trie = c_trie[0][c]

        if not exist:
            continue

        if c_trie[1]:
            ans += 1

    print(ans)


def make_trie(ns):
    trie = [{}, False]

    for st in ns:
        c_trie = trie

        for idx, c in enumerate(st):
            if c not in c_trie[0].keys():
                c_trie[0][c] = [{}, False]

            if idx == len(st)-1:
                c_trie[0][c][1] = True

            c_trie = c_trie[0][c]

    return trie




n, m = map(int, sys.stdin.readline().strip().split(" "))
ns = []
ms = []
for _ in range(n):
    ns.append(sys.stdin.readline().strip())

for _ in range(m):
    ms.append(sys.stdin.readline().strip())

solve()