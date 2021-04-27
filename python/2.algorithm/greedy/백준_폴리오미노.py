import sys


def solve():
    global s

    cur_idx = 0
    while cur_idx < len(s):
        if s[cur_idx] == '.':
            cur_idx += 1
            continue

        # A 가능한지
        possible = True
        for i in range(4):
            if cur_idx + i >= len(s):
                possible = False
                break

            if s[cur_idx + i] == '.':
                possible = False
                break

        if possible:
            for i in range(4):
                s[cur_idx + i] = 'A'
            cur_idx += 4
            continue

        # B 가능한지
        possible = True
        for i in range(2):
            if cur_idx + i >= len(s):
                possible = False
                break

            if s[cur_idx + i] == '.':
                possible = False
                break

        if possible:
            for i in range(2):
                s[cur_idx + i] = 'B'
            cur_idx += 2
            continue


        return print(-1)

    for c in s:
        print(c, end='')


s = list(sys.stdin.readline().strip())
solve()
