import sys


def solve(idx, cur):
    global n, k, cards





n = int(sys.stdin.readline().strip())
k = int(sys.stdin.readline().strip())
cards = []
nums = set()
for _ in range(n):
    cards.append(int(sys.stdin.readline().strip()))

solve(0, [])