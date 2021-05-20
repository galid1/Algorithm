import sys


def solve():
    global cmds

    max_num = 0
    cur_num = 0
    for a, b in cmds:
        cur_num -= a
        cur_num += b

        max_num = max(max_num, cur_num)

    print(max_num)





cmds = []
for i in range(4):
    a, b = map(int, sys.stdin.readline().strip().split(" "))
    cmds.append((a, b))

solve()
