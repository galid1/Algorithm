import sys


def solve(cmds):
    global ds
    up, down, left, right = 0, 0, 0, 0

    cx, cy, d = 0, 0, 0

    for cmd in cmds:
        if cmd == "L" or cmd == "R":
            if cmd == "L":
                d = (d - 1) % 4
            elif cmd == "R":
                d = (d + 1) % 4
        else:
            dx, dy = ds[d]
            if cmd == "F":
                cx, cy = cx + dx, cy + dy
            elif cmd == "B":
                cx, cy = cx - dx, cy - dy

            if cx < up:
                up = cx
            if cx > down:
                down = cx
            if cy < left:
                left = cy
            if cy > right:
                right = cy

    print((abs(up) + abs(down)) * (abs(left) + abs(right)))


ds = [[-1, 0], [0, 1], [1, 0], [0, -1]]
t = int(sys.stdin.readline().strip())
for _ in range(t):
    solve(list(sys.stdin.readline().strip()))
