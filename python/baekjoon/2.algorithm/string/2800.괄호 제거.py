import sys
from itertools import combinations


def solve():
    global s

    results = set()

    for pair_comb in make_pair_combs():
        origins = []
        for pair in pair_comb:
            left, right = pair
            origins.append((left, s[left]))
            origins.append((right, s[right]))

            s[left], s[right] = '', ''

        results.add(''.join(s))

        for idx, c in origins:
            s[idx] = c

    results = list(results)
    results.sort()

    for result in results:
        print(result)



def make_pair_combs():
    global s

    pairs = []
    stack = []
    for idx, c in enumerate(s):
        if c == '(':
            stack.append(idx)
        elif c == ')':
            pair_left = stack.pop()
            pair_right = idx

            pairs.append((pair_left, pair_right))

    comb_pairs = []

    for r in range(1, len(pairs)+1):
        for comb_pair in list(combinations(pairs, r)):
            comb_pairs.append(comb_pair)


    return comb_pairs


s = list(sys.stdin.readline().strip())
solve()
