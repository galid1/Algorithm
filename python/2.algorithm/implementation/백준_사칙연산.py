import sys

def solution(n, m):
    print(n + m)
    print(n - m)
    print(n * m)
    print(n // m)
    print(n % m)

n, m = map(int, sys.stdin.readline().split(" "))
solution(n, m)