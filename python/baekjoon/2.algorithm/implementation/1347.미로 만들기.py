import sys


def solve():
    global n, s

    # 한번 순회하면서, 좌표들을 모두 저장, 최대 가로 세로 길이 구하기

    maze = [['#' for _ in range(110)] for _ in range(110)]
    cx, cy = 55, 55
    maze[cx][cy] = '.'
    d = 0

    min_x, min_y, max_x, max_y = 55, 55, 55, 55

    for c in s:
        if c == "F":
            cx, cy = cx + ds[d][0], cy + ds[d][1]
            min_x, min_y = min(min_x, cx), min(min_y, cy)
            max_x, max_y = max(max_x, cx), max(max_y, cy)
            maze[cx][cy] = '.'
        else:
            d = turn(d, c)

    for i in range(min_x, max_x + 1):
        for j in range(min_y, max_y + 1):
            print(maze[i][j], end='')
        print()


def turn(cd, turn_direction):
    if turn_direction == "R":
        return (cd + 1) % 4

    else:
        return (cd - 1) % 4


ds = ((1, 0), (0, -1), (-1, 0), (0, 1))
n = int(sys.stdin.readline().strip())
s = sys.stdin.readline().strip()
solve()