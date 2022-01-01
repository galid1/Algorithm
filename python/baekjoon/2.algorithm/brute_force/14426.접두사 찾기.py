import sys


class Node:
    def __init__(self):
        self.links = {}
        self.cnt = 1


def solve():
    global n, m, nss, mss

    trie = make_trie(nss)

    ans = 0
    for ms in mss:
        tmp_ref = trie
        clear = True

        for c in ms:
            if c not in tmp_ref.links:
                clear = False
                break

            tmp_ref = tmp_ref.links[c]

        if clear:
            ans += 1

    print(ans)


def make_trie(nss):
    trie = Node()

    for ns in nss:
        tmp_ref: Node = trie
        for c in ns:
            if c in tmp_ref.links.keys():
                tmp_ref = tmp_ref.links[c]
                tmp_ref.cnt += 1

            else:
                new_node = Node()
                tmp_ref.links[c] = new_node
                tmp_ref = tmp_ref.links[c]

    return trie


n, m = map(int, sys.stdin.readline().strip().split(" "))
nss, mss = [], []
for _ in range(n):
    nss.append(tuple(sys.stdin.readline().strip()))

for _ in range(m):
    mss.append(tuple(sys.stdin.readline().strip()))

solve()
