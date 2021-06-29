import sys


def solution():
    global peos

    peos.sort(key= lambda x : int(x[0]))

    for peo in peos:
        print(peo[0], peo[1])


n = int(sys.stdin.readline())
peos = []
for i in range(n):
    peos.append(list(sys.stdin.readline().strip().split(" ")))
solution()