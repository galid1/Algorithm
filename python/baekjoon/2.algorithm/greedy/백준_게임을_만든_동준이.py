import sys


def solution():
    global n, lvs

    answer = 0

    for i in range(n-2, -1, -1):
        if lvs[i] >= lvs[i+1]:
            answer += lvs[i] - lvs[i+1] + 1
            lvs[i] = lvs[i+1] - 1

    print(answer)


n = int(sys.stdin.readline())
lvs = []
for i in range(n):
    lvs.append(int(sys.stdin.readline()))
solution()