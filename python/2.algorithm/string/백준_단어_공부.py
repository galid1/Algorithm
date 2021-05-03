import sys


def solve():
    global s

    g = {i:0 for i in range(ord('a'), ord('z')+1)}

    for c in s:
        g[ord(c)] += 1

    max_num_cnt = 0
    max_num_idx = 0
    max_cnt = -1

    for i, n in g.items():
        if n > max_cnt:
            max_cnt = n
            max_num_idx = i
            max_num_cnt = 1
            continue

        if n == max_cnt:
            max_num_cnt += 1

    if max_num_cnt >= 2:
        print("?")
    else:
        print(chr(max_num_idx).upper())



s = list(map(lambda c : c.lower(), sys.stdin.readline().strip()))
solve()