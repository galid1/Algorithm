import sys

def solve():
    global n

    ans = 0
    drainage = ''
    while True:
        drainage += '1'

        target = int(drainage)
        if n > target:
            continue

        if target%n == 0:
            return print(len(drainage))


while True:
    n = sys.stdin.readline().strip()

    if not n:
        exit()

    n = int(n)
    solve()