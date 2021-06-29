import sys

def solution(string):
    if not string.strip():
        print(0)
        return

    ss = string.strip().split(" ")
    print(len(ss))


s = sys.stdin.readline()
solution(s)
