import sys


def solution():
    global n, num
    print(sum(num))


n = int(sys.stdin.readline())
num = list(map(int, list(sys.stdin.readline().strip())))
solution()
