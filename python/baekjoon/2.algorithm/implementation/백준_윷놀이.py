import sys


def solve(inputs):
    global cmds

    zeros = 0
    for num in inputs:
        if num == '0':
            zeros += 1

    print(cmds[zeros])


cmds = {
    0: "E",
    1: "A",
    2: "B",
    3: "C",
    4: "D"
}
for _ in range(3):
    inputs = list(sys.stdin.readline().strip().split(" "))
    solve(inputs)