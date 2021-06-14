import sys

def solve():
    global n, m, ss, cmds

    for gender, number in cmds:
        if gender == 1:
            male(number)
        else:
            female(number)

    start = True
    for i in range(n):
        if i%20==0:
            if start:
                start = False
            else:
                print("")

        print(ss[i], end=' ')




def female(number):
    global ss, n

    idx = number - 1
    ss[idx] = 1 - ss[idx]

    l, r = idx-1, idx+1

    while l >= 0 and r < n:
        if ss[l] != ss[r]:
            break

        ss[l], ss[r] = 1 - ss[l], 1 - ss[r]
        l, r = l-1, r+1


def male(number):
    global ss, n

    idx = number - 1

    while idx < n:
        ss[idx] = 1 - ss[idx]
        idx += number



n = int(sys.stdin.readline().strip())
ss = list(map(int, sys.stdin.readline().strip().split(" ")))
m = int(sys.stdin.readline().strip())
cmds = []
for _ in range(m):
    cmds.append(list(map(int, sys.stdin.readline().strip().split(" "))))

solve()
