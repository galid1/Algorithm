import sys


def solve(cur, v_cnt, c_cnt, si):
    global l, c, cs

    if len(cur) == l:
        if v_cnt >= 1 and c_cnt >= 2:
            print(''.join(cur))
        return

    if l > len(cur) + (c - si):
        return

    for i in range(si, c):
        cur.append(cs[i])
        if cs[i] in vowels:
            solve(cur, v_cnt+1, c_cnt, i+1)
        else:
            solve(cur, v_cnt, c_cnt+1, i+1)
        cur.pop()


l, c = map(int, sys.stdin.readline().strip().split(" "))
vowels = {'a', 'i', 'o', 'u', 'e'}
cs = list(sys.stdin.readline().strip().split(" "))
cs.sort()

solve([], 0, 0, 0)