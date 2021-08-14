import sys
from collections import defaultdict

def solve():
    global trees, cnt

    trees = dict(sorted(trees.items(), key=lambda item: item[0]))

    for tree in trees.keys():
        print("%s %.4f" % (tree, trees[tree]/cnt*100))

trees = defaultdict(int)
cnt = 0
while True:
    tree = sys.stdin.readline().strip()

    if not tree:
        break

    cnt += 1
    trees[tree] += 1

solve()

