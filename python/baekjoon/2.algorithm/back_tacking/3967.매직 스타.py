import sys
from collections import deque


def solve():
    global coords_line, lines, q, info

    if not q:
        return True

    x, y = q.popleft()

    for num in range(1, 13):
        if not valid(x, y, num):
            continue

        if num in visited:
            continue

        for link in coords_line[(x, y)]:
            lines[link].append(num)
        visited.add(num)
        info[x][y] = chr(num+64)

        res = solve()
        if res:
            return True

        info[x][y] = 'x'
        for link in coords_line[(x, y)]:
            lines[link].pop()
        visited.remove(num)

    q.appendleft([x, y])
    return False


def valid(x, y, num):
    global lines, coords_line, info

    for link in coords_line[(x, y)]:
        sums, cnt = sum(lines[link]), len(lines[link])

        if cnt+1 == 4:
            if sums + num != 26:
                return False
        else:
            if sums + num >= 26:
                return False

    return True


def init():
    global info, visited

    # 좌표가 속한 라인
    coords_line = {
        (0, 4): ["tl", "tr"],
        (1, 1): ["r1", "lr"],
        (1, 3): ["r1", "tl"],
        (1, 5): ["r1", "tr"],
        (1, 7): ["r1", "rl"],
        (2, 2): ["tl", "lr"],
        (2, 6): ["tr", "rl"],
        (3, 1): ["r2", "tl"],
        (3, 3): ["r2", "lr"],
        (3, 5): ["r2", "rl"],
        (3, 7): ["r2", "tr"],
        (4, 4): ["lr", "rl"]
    }

    # 라인별 정보
    lines = {
        "tl": [],
        "tr": [],
        "r1": [],
        "r2": [],
        "lr": [],
        "rl": []
    }
    # 빈 큐
    q = deque()

    for i in range(5):
        for j in range(9):
            cur = info[i][j]

            if cur == '.':
                continue
            elif cur == 'x':
                q.append([i, j])
            else:
                num = ord(cur) - 64
                visited.add(num)
                for link in coords_line[(i, j)]:
                    lines[link].append(num)

    return coords_line, lines, q


info = []
for _ in range(5):
    info.append(list(sys.stdin.readline().strip()))

visited = set()
coords_line, lines, q = init()
solve()

for i, ans in enumerate(info):
    print(''.join(ans))
