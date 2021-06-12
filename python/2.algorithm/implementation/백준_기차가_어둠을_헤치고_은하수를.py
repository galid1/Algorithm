import sys


def solve():
    global n, m, cmds, trains

    for cmd in cmds:
        do_command(cmd)

    can_trains = set()

    for train in trains:
        bit_train = ''.join(train)
        can_trains.add(bit_train)

    print(len(can_trains))


def do_command(cmd):
    global trains

    ti = cmd[1]-1

    if cmd[0] == 1:
        seat = cmd[2]-1
        if trains[ti][seat] == '0':
            trains[ti][seat] = '1'

    elif cmd[0] == 2:
        seat = cmd[2]-1
        if trains[ti][seat] == '1':
            trains[ti][seat] = '0'

    elif cmd[0] == 3:
        for seat in range(19, 0, -1):
            trains[ti][seat] = trains[ti][seat-1]
        trains[ti][0] = '0'

    elif cmd[0] == 4:
        for seat in range(19):
            trains[ti][seat] = trains[ti][seat+1]
        trains[ti][19] = '0'


n, m = map(int, sys.stdin.readline().strip().split(" "))
cmds = []
for _ in range(m):
    cmds.append(list(map(int, sys.stdin.readline().strip().split(" "))))

trains = [['0' for _ in range(20)] for _ in range(n)]

solve()

# a = [1, 1, 0, 1, 1]
# for i in range(len(a)-1):
#     a[i] = a[i+1]
# a[len(a)-1] = 0
#
# print(a)