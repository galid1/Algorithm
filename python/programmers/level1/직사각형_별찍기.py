import sys

def solution(a, b):
    print((("*" * a) + "\n") * b)

a, b = map(int, sys.stdin.readline().split(" "))
solution(a, b)