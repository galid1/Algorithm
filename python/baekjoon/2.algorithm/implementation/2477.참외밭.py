import sys

def solve(num, lines):
    hor_idx, hor_len = -1, -1
    ver_idx, ver_len = -1, -1
    last_idx = -1

    for idx, info in enumerate(lines):
        dir, length = info

        if dir == 1 or dir == 2:
            if length > hor_len:
                hor_len = length
                hor_idx = idx
                last_idx = idx
        else:
            if length > ver_len:
                ver_len = length
                ver_idx = idx
                last_idx = idx

    if hor_idx > ver_idx:
        hor_idx, ver_idx = ver_idx, hor_idx

    large_rec = hor_len * ver_len
    small_rec = lines[(last_idx+2)%6][1] * lines[(last_idx+3)%6][1]
    if last_idx == 5 and hor_idx == 0:
        small_rec = lines[(last_idx - 2) % 6][1] * lines[(last_idx - 3) % 6][1]

    return print((large_rec-small_rec) * num)


num = int(sys.stdin.readline().strip())
lines = []
for _ in range(6):
    dir, line = map(int, sys.stdin.readline().strip().split(" "))
    lines.append([dir, line])

solve(num, lines)


# 5
# 4 10
# 2 10
# 4 10
# 2 10
# 3 20
# 1 20


# 5
# 3 20
# 1 10
# 4 10
# 1 10
# 4 10
# 2 20

# 5
# 1 10
# 4 10
# 1 10
# 4 10
# 2 20
# 3 20


# 7
# 3 30
# 1 60
# 3 20
# 1 100
# 4 50
# 2 160


# 7
# 2 160
# 3 30
# 1 60
# 3 20
# 1 100
# 4 50
