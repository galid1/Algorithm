import sys


def solve():
    global kx, ky, sx, sy, n, moves, cmds, coords

    for move in moves:
        nkx, nky = kx + cmds[move][0], ky + cmds[move][1]

        if not is_valid(nkx, nky):
            continue

        if nkx == sx and nky == sy:
            nsx, nsy = sx + cmds[move][0], sy + cmds[move][1]

            if not is_valid(nsx, nsy):
                continue
            sx, sy = nsx, nsy

        kx, ky = nkx, nky

    print(coords[ky], end='')
    print(kx)
    print(coords[sy], end='')
    print(sx)


def is_valid(x, y):
    if 1 <= x <= 8 and 1 <= y <= 8:
        return True
    return False


cmds = {
    "B": (-1, 0),
    "L": (0, -1),
    "R": (0, 1),
    "T": (1, 0),
    "RT": (1, 1),
    "LT": (1, -1),
    "RB": (-1, 1),
    "LB": (-1, -1)
}
coords = {
    "A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8,
    1: "A", 2: "B", 3: "C", 4: "D", 5: "E", 6: "F", 7: "G", 8: "H"
}
king, stone, n = sys.stdin.readline().strip().split(" ")
king = list(king)
ky, kx = coords[king[0]], int(king[1])
sy, sx = coords[stone[0]], int(stone[1])
stone = list(stone)
moves = []
for _ in range(int(n)):
    moves.append(sys.stdin.readline().strip())
solve()



# A1 A2 5
# R
# R
# RT
# T
# T